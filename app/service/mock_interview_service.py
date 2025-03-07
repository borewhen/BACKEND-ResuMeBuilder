from fastapi import FastAPI, HTTPException, UploadFile
import requests
import os
from app.models import MockInterview, Category, Subcategory
import openai
import tempfile
from app.service.job_service import get_company_name_and_job_position
from sqlalchemy.orm import joinedload

LINKEDIN_SCRAPER_API_KEY=os.getenv("LINKEDIN_SCRAPER_API_KEY", "dummy_key")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "dummy_key")


def parse_skills_from_job(db, job_id, mock_interview_id):
    """
    parse job description and post this to DB
    job_description (str)
    """
    try:
        response = response = requests.get(
            f"https://api.scrapingdog.com/linkedinjobs",
            params={"api_key": LINKEDIN_SCRAPER_API_KEY, "job_id": {job_id}},
        )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Error fetching jobs: {response.text}")

        job_detail = response.json()

        # extract skills category from job_desc
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    the following is a job description:

                    ---
                    {job_detail[0].get("job_description", "No description available.")}
                    ---
                    
                    what are the technical skills required and group these technical skills into categories?
                    group related specific skills such as (html, css, js) under a broader category "Frontend Development", or (nodejs, python, kafka) is grouped and category "Backend Development".  
                    Give me 4 skill categories at max, it's okay to give less if there is none.
                    Give it in the following format in coma seperated without space eg. "Backend Development,Frontend Development,AI".
                    Also don't include redundant topics such as "monitoring and logging", "cloud" and "devops" should be only under one category "devops"
                    """
                }
            ]
        )

        # get sub categories skill for each category in job_desc
        categories = completion["choices"][0]["message"]["content"].strip().split(",")
        category_map = insert_categories(db, mock_interview_id, categories)

        sub = []
        for category in categories:
            completion = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        for the following is a job description:

                        ---
                        {job_detail[0].get("job_description", "No description available.")}
                        ---
                        
                        from the following job description, can you list at max 3 specific subskills that belongs to the category of {category}, if there are less than 3 subskills, it's okay to leave the rest blank.
                        For example under the topic of Devops, we have kubernetes, docker and aws. So diplay it in the following format in a comma seperated without space "Kubernetes,Docker,AWS".
                        Just give it in this format without and leading or post sentence.
                        """
                    }
                ]
            )
            subcategories = completion["choices"][0]["message"]["content"].strip().split(",")
            for subcategory in subcategories:
                sub.append(Subcategory(category_id=category_map[category], subcategory_name=subcategory))
        
        insert_subcategories(db, sub)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500)


def create_mock_interview(db, job_id: int, user_id: int):
    """
    Creates a new mock interview entry if it does not already exist.
    db (Session): SQLAlchemy database session.
    job_id (int): The job ID.
    user_id (int): The user ID.
    """
    existing_mock_interview = (
        db.query(MockInterview)
        .filter(MockInterview.job_id == job_id, MockInterview.user_id == user_id)
        .options(joinedload(MockInterview.categories).joinedload(Category.subcategories))
        .first()
    )
    
    if existing_mock_interview:
        res = []
        for category in existing_mock_interview.categories:
            res.append({
                "category_id": category.category_id,
                "category_name": category.category_name,
                "subcategories": [{
                    "subcategory_id": sub.subcategory_id,
                    "status": sub.status,
                    "subcategory_name": sub.subcategory_name
                } for sub in category.subcategories]
            })
        return res, True

    job_detail = get_company_name_and_job_position(job_id)
    new_mock_interview = MockInterview(job_id=job_id, user_id=user_id, company_name=job_detail["company_name"], job_position=job_detail["job_position"])
    db.add(new_mock_interview)
    db.flush()
    return new_mock_interview, False


async def get_transcript(file: UploadFile):
    """
    Creates a transcript from an audio file.
    file (UploadFile): The audio file to transcribe.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio:
            temp_audio.write(await file.read())
            temp_audio_path = temp_audio.name
        
        wav_audio_path = temp_audio_path.replace('.webm', '.wav')
        os.system(f"ffmpeg -i {temp_audio_path} -ar 16000 -ac 1 -c:a pcm_s16le {wav_audio_path}")
    
        with open(wav_audio_path, "rb") as audio_file:
            transcipt = openai.Audio.transcribe("whisper-1", audio_file)
            
        os.remove(temp_audio_path)
        os.remove(wav_audio_path)
        
        return {"transcript": transcipt["text"]}
    except Exception as e:
        return {"error": str(e)}


def insert_categories(db, mock_interview_id, categories):
    """
    Creates category entries if they do not already exist.
    db (Session): SQLAlchemy database session.
    mock_interview_id (int): The mock_interview_id.
    categories (list[str]): The list of categories.
    """
    category_objects = [Category(mock_interview_id=mock_interview_id, category_name=name) for name in categories]
    
    db.bulk_save_objects(category_objects, return_defaults = True)
    db.flush()

    category_map = {category.category_name: category.category_id for category in category_objects}
    return category_map


def insert_subcategories(db, subcategories):
    """
    Creates category entries if they do not already exist.
    db (Session): SQLAlchemy database session.
    subcategories (list[Subcategories]): The list of subcategories.
    """
    db.bulk_save_objects(subcategories)
    db.flush()


def get_mock_interview_topics(db, job_id, user_id):
    """
    Get mock_interview category and subcategory.
    db (Session): SQLAlchemy database session.
    subcategories (list[Subcategories]): The list of subcategories.
    """
    mock_interview = (
        db.query(MockInterview)
        .filter(MockInterview.job_id == job_id, MockInterview.user_id == user_id)
        .options(joinedload(MockInterview.categories).joinedload(Category.subcategories))
        .first()
    )

    res = []
    for category in mock_interview.categories:
        res.append({
            "category_id": category.category_id,
            "category_name": category.category_name,
            "subcategories": [{
                "subcategory_id": sub.subcategory_id,
                "status": sub.status,
                "subcategory_name": sub.subcategory_name
            } for sub in category.subcategories]
        })
    return res