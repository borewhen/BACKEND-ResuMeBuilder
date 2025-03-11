from fastapi import FastAPI, HTTPException, UploadFile
import requests
import os
from app.models import MockInterview, Category, Subcategory, Question, Answer
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


def initialize_subcategory_interview_session(db, subcategory_id):
    """
    creates a question for that subcategory if the subcategory for the user doesn't have any question yet.
    Returns the result in the format:
    {
        "question": [],
        "answer": [],
        "feedback": [],
        "status": []
    }
    """
    subcategory_name = (
        db.query(Subcategory)
        .with_entities(Subcategory.subcategory_name)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )

    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""
                the following is an interview topic:

                ---
                {subcategory_name}
                ---
                
                please provide one technical interview question regarding this topic. Just provide the question text directly without any introductory text or potential answers
                An example format is the following "What is the difference between git pull or git fetch?""
                """
            }
        ]
    )
    question_name = completion["choices"][0]["message"]["content"].strip().split(",")
    new_question = Question(
        question_name=question_name[0],
        subcategory_id=subcategory_id
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return {
        "question": [new_question.question_name],
        "answer": [],
        "feedback": [],
        "status": True
    }


def get_existing_interview_session_info(db, user_id, subcategory_id):
    """
    db (Session): SQLAlchemy database session.
    Returns the result in the format:
    {
        "question": [],
        "answer": [],
        "feedback": [],
        "status": []
    }
    """
    subcategory_status = (
        db.query(Subcategory)
        .with_entities(Subcategory.status)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )

    questions = (
        db.query(Question)
        .join(Subcategory, Question.subcategory_id == Subcategory.subcategory_id)
        .join(Category, Subcategory.category_id == Category.category_id)
        .join(MockInterview, Category.mock_interview_id == MockInterview.mock_interview_id)
        .filter(MockInterview.user_id == user_id, Subcategory.subcategory_id == subcategory_id)
        .all()
    )

    if not questions:
       return initialize_subcategory_interview_session(db, subcategory_id)

    print(f">>>>>> questions {questions}")
    question_list = []
    answer_list = []
    feedback_list = []
    for question in questions:
        question_list.append(question.question_name)
        
        if question.answer:
            answer_list.append(question.answer.answer)
            feedback_list.append(question.answer.feedback)

    return {
        "question": question_list,
        "answer": answer_list,
        "feedback": feedback_list,
        "status": subcategory_status
    }