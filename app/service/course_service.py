from fastapi import FastAPI, HTTPException, UploadFile
import requests
import os
from app.models import Chapter, Unit, Course, MockInterview
import openai
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from app.service.job_service import get_company_logo_from_job_id
import re
from youtube_transcript_api import YouTubeTranscriptApi

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "dummy_key")


def get_all_courses(db, user_id):
    """
    Retrieve all course accessible by the user
    """
    courses = (
        db.query(Course)
        .filter(Course.user_id == user_id)
        .all()
    )
    return [course.to_dict() for course in courses]


def get_course_by_id(db, course_id, user_id):
    """
    Retrieve a single course by course_id for a specific user.
    """
    course = (
        db.query(Course)
        .filter(Course.course_id == course_id, Course.user_id == user_id)
        .first()
    )

    if not course:
        raise HTTPException(status_code=404, detail=f"Course not found")
    return course.to_dict()


def create_course(db, mock_interview_id, user_id):
    """
    Create a new course based on failed topics in mock interview
    """
    mock_interview = (
        db.query(MockInterview)
        .filter(MockInterview.mock_interview_id == mock_interview_id, MockInterview.user_id == user_id)
        .first()
    )

    if not mock_interview:
        raise HTTPException(status_code=404, detail=f"Course not found")
    
    company_logo = get_company_logo_from_job_id(mock_interview.job_id)

    new_course = Course(mock_interview_id=mock_interview_id, image_url=company_logo, user_id=user_id)
    db.add(new_course)
    db.flush()

    all_chapters = []
    failed_topics = mock_interview.failed_topics.split()
    for unit_name in failed_topics:
        prompt_prefix = f"This is a course with given the unit of the topic: {unit_name}, "
        visited = ""
        chapter_list = []

        new_unit = Unit(course_id=new_course.course_id, unit_name=unit_name)
        db.add(new_unit)
        db.flush()

        for _ in range(3):
            completion = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": prompt_prefix + f"""
                        Provide me with a subtopic for this unit in less than 10 words that doesn't exist yet in ${visited}. Just provide the subtopic directly without any introductory text.
                        For eg for the unit Javascript, the subtopics can be "Understanding callbacks and async".
                        """
                    }
                ]
            )

            raw_chapter_name = completion["choices"][0]["message"]["content"].strip()
            chapter_name = re.sub(r'^"(.*)"$', r'\1', raw_chapter_name)
            chapter_list.append(chapter_name)
            visited += f"{chapter_name}, "

            all_chapters.append({
                "chapter_name": chapter_name,
                "unit_id": new_unit.unit_id
            })

    db.bulk_insert_mappings(Chapter, all_chapters)
    db.commit()


def create_course_video(db, course_id):
    """
    Generate course video for each topic
    """
    chapters = (
        db.query(Chapter)
        .join(Unit)
        .filter(Unit.course_id == course_id)
        .options(joinedload(Chapter.unit))
        .all()
    )

    if not chapters:
        raise HTTPException(status_code=404, detail=f"Course not found")

    for chapter in chapters:
        unit_name = chapter.unit.unit_name
        chapter_name = chapter.chapter_name

        yt_query_response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Given the chapter '{chapter_name}' from the unit '{unit_name}', "
                        "Provide me with a YouTube search query regarding the following chapter for the given topic WITHOUT QUOTATION MARKS in 20 words or less."
                    ),
                }
            ],
        )

        yt_query = yt_query_response.choices[0].message.content.strip()
        YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
        youtube_url = (
            f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1"
            f"&order=relevance&q={yt_query}&type=video&key={YOUTUBE_API_KEY}&videoCaption=closedCaption"
        )

        video_response = requests.get(youtube_url).json()
        if "items" not in video_response or not video_response["items"]:
            print(f"No relevant video found for chapter: {chapter_name}")
            continue

        video_data = video_response["items"][0]
        video_id = video_data["id"]["videoId"]
        video_title = video_data["snippet"]["title"]
        video_thumbnail = video_data["snippet"]["thumbnails"]["default"]["url"]

        try:
            transcript = YouTubeTranscriptApi().fetch(video_id)
            transcript_text = " ".join([snippet.text for snippet in transcript.snippets])[:500]
        except Exception as e:
            print(f"Could not fetch transcript for video {video_id}: {e}")
            transcript_text = "Transcript not available."

        summary_response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": (
                        transcript_text +
                        " Summarize the following transcript in 250 words or less "
                        "without referencing the video or channel itself. Summarize only the educational content."
                    ),
                }
            ],
        )

        summarized_transcript = summary_response.choices[0].message.content.strip()
        db.query(Chapter).filter(Chapter.chapter_id == chapter.chapter_id).update({
            "video_thumbnail": video_thumbnail,
            "video_title": video_title,
            "video_id": video_id,
            "video_transcript": summarized_transcript,
        })

    db.commit()
