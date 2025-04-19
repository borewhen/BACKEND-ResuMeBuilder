from fastapi import FastAPI, HTTPException, UploadFile
import requests
import os
from app.models import MockInterview, Category, Subcategory, Question, Answer
import openai
from app.service.job_service import get_company_name_and_job_position
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from app.service.mapping_service import question_map, question_map_2
import time

LINKEDIN_SCRAPER_API_KEY=os.getenv("LINKEDIN_SCRAPER_API_KEY", "dummy_key")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "dummy_key")


def parse_skills_from_job(db, job_id, mock_interview_id):
    """
    parse job description and post this to DB
    job_description (str)
    """
    try:
        time.sleep(3)
        if job_id == 42012811001:
            categories = ["Frontend Engineering", "LLM & AI System", "Backend Engineering"]
            category_map = insert_categories(db, mock_interview_id, categories)
            sub = [Subcategory(category_id=category_map["Frontend Engineering"], subcategory_name="Typescript"),
                   Subcategory(category_id=category_map["Frontend Engineering"], subcategory_name="Next.js"),
                   Subcategory(category_id=category_map["LLM & AI System"], subcategory_name="Retrieval-Augmented Generation (RAG)"),
                   Subcategory(category_id=category_map["LLM & AI System"], subcategory_name="Embeddings"),
                   Subcategory(category_id=category_map["Backend Engineering"], subcategory_name="API Design"),
                   Subcategory(category_id=category_map["Backend Engineering"], subcategory_name="Serverless Architectures")]
            insert_subcategories(db, sub)
            return
        
        if job_id == 42012811002:
            categories = ["Data Analysis & Modelling", "Data Tools & Technologies"]
            category_map = insert_categories(db, mock_interview_id, categories)
            sub = [Subcategory(category_id=category_map["Data Analysis & Modelling"], subcategory_name="Data Preprocessing"),
                   Subcategory(category_id=category_map["Data Analysis & Modelling"], subcategory_name="Feature Engineering"),
                   Subcategory(category_id=category_map["Data Analysis & Modelling"], subcategory_name="Model Evaluation"),
                   Subcategory(category_id=category_map["Data Tools & Technologies"], subcategory_name="SQL Databases"),
                   Subcategory(category_id=category_map["Data Tools & Technologies"], subcategory_name="Visualization Tools"),
                   Subcategory(category_id=category_map["Data Tools & Technologies"], subcategory_name="Python for Data Science")]
            insert_subcategories(db, sub)
            return
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
                    
                    What are the technical skills required and group these technical skills into categories?
                    group related specific skills such as (html, css, js) under a broader category "Frontend Development", or (nodejs, python, kafka) is grouped and category "Backend Development".  
                    Do not include non-technical skills such as Data communication, project management etc
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
                "mock_interview_id": existing_mock_interview.mock_interview_id,
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

    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        return create_mock_interview(db, job_id, user_id)

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
            "mock_interview_id": mock_interview.mock_interview_id,
            "category_id": category.category_id,
            "category_name": category.category_name,
            "subcategories": [{
                "subcategory_id": sub.subcategory_id,
                "status": sub.status,
                "subcategory_name": sub.subcategory_name
            } for sub in category.subcategories]
        })
    return res

def get_jobid_from_subcategory(db, subcategory_id):
    """
    Get job_id from subcategory
    db (Session): SQLAlchemy database session.
    subcategories (list[Subcategories]): The list of subcategories.
    """
    job_id = (
        db.query(MockInterview.job_id)
        .join(Category, Category.mock_interview_id == MockInterview.mock_interview_id)
        .join(Subcategory, Subcategory.category_id == Category.category_id)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )
    return job_id

def initialize_subcategory_interview_session(db, subcategory_id, user_id):
    """
    creates a question for that subcategory if the subcategory for the user doesn't have any question yet.
    """
    job_id = get_jobid_from_subcategory(db, subcategory_id)
 
    questions = get_user_questions(db, user_id, subcategory_id)
    subcategory_name = (
        db.query(Subcategory)
        .with_entities(Subcategory.subcategory_name)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )

    if job_id == 42012811001 or job_id == 42012811002:
        category_name = (
            db.query(Category.category_name)
            .join(Subcategory, Subcategory.category_id == Category.category_id)
            .filter(Subcategory.subcategory_id == subcategory_id)
            .scalar()
        )
        questions_list = question_map[category_name][subcategory_name] if job_id == 42012811001 else question_map_2[category_name][subcategory_name]
        for question in questions_list: 
            new_question = Question(question_name=question["question"], subcategory_id=subcategory_id)
            db.add(new_question)
            db.flush()
            answer = Answer(
                question_id=new_question.question_id,
                answer=question["answer"],
                feedback=question["feedback"]
            )
            db.add(answer)
            db.flush()
            
        db.commit()
        return
    
    if questions:
        raise HTTPException(status_code=400, detail=f"interview session for {subcategory_name} has been initialized")

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
    question_name = completion["choices"][0]["message"]["content"].strip()
    print(f"question_name: {question_name}")
    new_question = Question(
        question_name=question_name,
        subcategory_id=subcategory_id
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)


def get_existing_interview_session_info(db, user_id, subcategory_id):
    """
    db (Session): SQLAlchemy database session.
    Returns the result in the format:
    {
        "question": [],
        "answer": [],
        "feedback": [],
        "status": bool
    }
    """
    job_id = get_jobid_from_subcategory(db, subcategory_id)
    if job_id == 42012811001 or job_id == 42012811002:
        subcategory_status = (
            db.query(Subcategory)
            .with_entities(Subcategory.status)
            .filter(Subcategory.subcategory_id == subcategory_id)
            .scalar()
        )
        questions = get_user_questions(db, user_id, subcategory_id)
        question_list = []
        answer_list = []
        feedback_list = []
        
        for question in questions:
            question_list.append(question.question_name)
            if question.answer and not question.answer.answer:
                break
            elif question.answer:
                answer_list.append(question.answer.answer)
                feedback_list.append(question.answer.feedback)
        
        return {
            "questions": question_list,
            "answers": answer_list,
            "feedbacks": feedback_list,
            "status": subcategory_status   
        }
    subcategory_status = (
        db.query(Subcategory)
        .with_entities(Subcategory.status)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )

    questions = get_user_questions(db, user_id, subcategory_id)
    question_list = []
    answer_list = []
    feedback_list = []
    for question in questions:
        question_list.append(question.question_name)
        
        if question.answer:
            answer_list.append(question.answer.answer)
            feedback_list.append(question.answer.feedback)
        
    return {
        "questions": question_list,
        "answers": answer_list,
        "feedbacks": feedback_list,
        "status": subcategory_status
    }


def get_user_questions(db, user_id, subcategory_id):
    """
    db (Session): SQLAlchemy database session.
    user_id (int): The user ID.
    subcategory_id (int): The subcategory ID.
    """
    questions = (
        db.query(Question)
        .join(Subcategory, Question.subcategory_id == Subcategory.subcategory_id)
        .join(Category, Subcategory.category_id == Category.category_id)
        .join(MockInterview, Category.mock_interview_id == MockInterview.mock_interview_id)
        .filter(MockInterview.user_id == user_id, Subcategory.subcategory_id == subcategory_id)
        .order_by(Question.question_id.asc())
        .all()
    )
    return questions


def update_answer(db, user_id, subcategory_id, user_answer):
    job_id = get_jobid_from_subcategory(db, subcategory_id)
    if job_id == 42012811001 or job_id == 42012811002:        
        questions = get_user_questions(db, user_id, subcategory_id)
        
        answered_questions = 0
        for question in questions:
            answered_questions += 1
            if question.answer and not question.answer.answer:
                question.answer.answer = user_answer
                db.commit()
                break
        
        if answered_questions == 3:
            subcategory = db.query(Subcategory).filter(Subcategory.subcategory_id == subcategory_id).first()
            if subcategory:
                subcategory.status = False
                db.commit()
        return
        
        
    latest_question = (
        db.query(Question)
        .join(Subcategory, Question.subcategory_id == Subcategory.subcategory_id)
        .join(Category, Subcategory.category_id == Category.category_id)
        .join(MockInterview, Category.mock_interview_id == MockInterview.mock_interview_id)
        .filter(MockInterview.user_id == user_id, Subcategory.subcategory_id == subcategory_id)
        .order_by(desc(Question.question_id))
        .first()
    )

    existing_answer = (
        db.query(Answer)
        .filter(Answer.question_id == latest_question.question_id)
        .first()
    )

    if not existing_answer:
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Question: {latest_question.question_name}

                    Answer: {user_answer}

                    Provide constructive feedback on this answer. Mention if it's correct, what can be improved, and how the response could be better. Give the feedback directly without any introductory text.
                    For eg. Your answer is correct but lacks depth. You could mention about types of indexes, tradoffs and how indexes are stored internally! Limit this to 100 words"
                    """
                }
            ]
        )

        feedback = completion["choices"][0]["message"]["content"].strip()
        answer = Answer(
            question_id=latest_question.question_id,
            answer=user_answer,
            feedback=feedback
        )
        db.add(answer)
        db.flush()

    questions = get_user_questions(db, user_id, subcategory_id)
    subcategory = db.query(Subcategory).filter(Subcategory.subcategory_id == subcategory_id).first()
    # update subcategory status if question length is 5
    if len(questions) == 1:
        if subcategory:
            subcategory.status = False

    # generate new question
    if subcategory.status:
        previous_questions = [
            question.question_name for question in questions
        ]
        new_question_text = generate_new_question(db, subcategory_id, user_id, previous_questions)
        new_question = Question(
            subcategory_id=subcategory_id,
            question_name=new_question_text
        )
        db.add(new_question)
        db.flush()
    
    db.commit()


def generate_new_question(db, subcategory_id, user_id, previous_questions):
    """
    creates a new question for that subcategory
    """
    prompt_content = f"""
    You are an expert technical interviewer. Your task is to generate a **unique** technical interview question for the following topic.

    **Topic:** {subcategory_id}

    **Previously asked questions:** 
    {', '.join(previous_questions) if previous_questions else "None"}

    **Instructions:**
    - Do NOT repeat any of the previously asked questions.
    - The question should be challenging and test in-depth understanding.
    - Ensure the question is different in wording and concept from previous ones.

    Generate one unique interview question related to this topic. Just provide the question text directly without any introductory text or potential answers
    An example format is the following "What is the difference between git pull or git fetch?""
    """

    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_content}]
    )

    new_question = completion["choices"][0]["message"]["content"].strip()
    return new_question


def generate_subcategory_summary(db, subcategory_id, user_id):
    """
    return subcategory summary
    {
        summary: str
    }
    """
    job_id = get_jobid_from_subcategory(db, subcategory_id)
    if job_id == 42012811001 or job_id == 42012811002:
        curr_summary = db.query(Subcategory).filter(Subcategory.subcategory_id == subcategory_id).first()
        if curr_summary and curr_summary.summary:
            return curr_summary.summary
        
        time.sleep(3)
        curr_summary.summary = "summary template"
        db.commit()
        return curr_summary.summary
    
    subcategory_status = (
        db.query(Subcategory)
        .with_entities(Subcategory.status)
        .filter(Subcategory.subcategory_id == subcategory_id)
        .scalar()
    )

    if subcategory_status:
        return ""
    
    subcategory = db.query(Subcategory).filter(Subcategory.subcategory_id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")

    if subcategory.summary and subcategory.summary.strip():
        return subcategory.summary

    interview_session = get_existing_interview_session_info(db, user_id, subcategory_id)
    interview_text = ""

    for i in range(len(interview_session["questions"])):
        question = interview_session["questions"][i]
        answer = interview_session["answers"][i]
        feedback = interview_session["feedbacks"][i]

        interview_text += f"""

        Question_{i+1}: {question}
        Answer_{i+1}: {answer}
        Feedback_{i+1}: {feedback}

        """

    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""
                You are an expert technical interviewer. Your task is to judge the result of interview based on the interview transcript given.

                **Topic:** {subcategory_id}

                **Interview Transcript:** 
                {interview_text}

                **Instructions:**
                - Based on the feedback on the answers of each question, generate an overall summary/feedback on the user performance on their mastery of the topics
                - The summary should concludes whether the user has sufficiently passed the interview or not
                - Give an explanation on which area to improve on for the user to pass the interview
                - Provide a suggested answer to the question without introductory text


                Just provide the summary text for the feedback of the OVERALL interview directly without any introductory text
                An example format is the following "Candidate has demonstrated strong technical understanding in SQL database, however candidate is lacking knowledge on the use case for NoSQL database. Therefore, candidate did not passed the interview."
                """
            }
        ]
    )

    summary_text = completion["choices"][0]["message"]["content"].strip()
    db.query(Subcategory).filter(Subcategory.subcategory_id == subcategory_id).update({"summary": summary_text})
    db.commit()
    return summary_text


def generate_mock_interview_summary(db, job_id, user_id):
    """
    return the summary of the mock interview
    """
    if job_id == 42012811001 or job_id == 42012811002:
        curr_summary = db.query(MockInterview).filter(MockInterview.job_id == job_id, MockInterview.user_id == user_id).first()
        if curr_summary and curr_summary.summary:
            return {
            "summary": curr_summary.summary,
            "failed_topics": curr_summary.failed_topics
        }
    
        time.sleep(7)
        summary = "Candidate has demonstrated strong technical understanding in SQL database, however candidate is lacking knowledge on the use case for NoSQL database. Therefore, candidate did not passed the interview." if job_id == 42012811001 else "Overall, the interview responses demonstrate a foundational understanding of key data science concepts, with strong answers in areas like feature selection, model comparison, and the use of Python libraries across the data pipeline. However, there are notable gaps in critical subcategories such as Data Preprocessing and Model Evaluation, where overly simplistic or incomplete approaches were given for handling missing values, outliers, and performance metrics like precision and recall. Additionally, while the candidate shows familiarity with SQL operations and visualization tools, certain responses lacked depth or clarity, suggesting room for growth in articulating and applying best practices. With more experience and focus on nuanced problem-solving strategies, the candidate has strong potential to strengthen their data science proficiency."
        failed_topics = "Retrieval-Augmented Generation (RAG),Embeddings,Serverless Architectures" if job_id == 42012811001 else "Data Preprocessing, Model Evaluation"
        curr_summary.summary = summary
        curr_summary.failed_topics = failed_topics
        db.commit()
        return {
            "summary": summary,
            "failed_topics": failed_topics
        }
        
    current_mock_interview = (
        db.query(MockInterview)
        .filter(MockInterview.job_id == job_id, MockInterview.user_id == user_id)
        .options(joinedload(MockInterview.categories).joinedload(Category.subcategories))
        .first()
    )

    if not current_mock_interview:
        return HTTPException(status_code=404, detail="MockInterview not found")

    if current_mock_interview.summary and current_mock_interview.failed_topics:
        return {
            "summary": current_mock_interview.summary,
            "failed_topics": current_mock_interview.failed_topics
        }

    sub_summary = []
    # check if all the status of the subcategories are all false
    flag = True
    categories = current_mock_interview.categories
    for category in categories:
        subcategories = category.subcategories
        for subcategory in subcategories:
            if subcategory.status:
                flag = False
                break

            sub_summary.append({
                "topic": subcategory.subcategory_name,
                "summary": subcategory.summary
            })

    # summary "" if not all test is done
    if not flag:
        return {
            "summary": "",
            "failed_topics": ""
        }
    
    # generate summary of whole interview
    topic_summary = ""
    for i in range(len(sub_summary)):
        topic_summary += f""""

        {i+1}. topic name: {sub_summary[i]["topic"]}
        {i+1}. interview result summary: {sub_summary[i]["summary"]}

        """
    
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""
                You are an expert technical interviewer. Your task is judge interview result based on the topics tested in the interview and note down the topics that the candidate failed.

                {topic_summary}

                **Instructions:**
                - Create an overall summary text of the interview, denoting which topic candidate did well and which did not.

                Just provide the summary text for the feedback of the OVERALL interview directly without any introductory text
                An example format is the following "Candidate possesses strong frontend development skill, showing strong fundamental in React and CSS. However, candidate lack expertise in system design and backend knowledge which is essential for this fullstack development role"
                """
            }
        ]
    )

    summary_text = completion["choices"][0]["message"]["content"].strip()
    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""
                You are an expert technical interviewer. Your task is to note down which topic the candidate failed. If there is no summary, then it is assumed to be good

                {topic_summary}

                **Instructions:**
                - From the given interview summary/result of each topic, list down which topics did the candidate failed

                Just provide the list of topics that candidate FAILED without any introductory text and give it in a comma seperated value without space
                An example format is the following "SQL,Kubernetes,AWS"
                """
            }
        ]
    )

    failed_topics = completion["choices"][0]["message"]["content"].strip()
    current_mock_interview.summary = summary_text
    current_mock_interview.failed_topics = failed_topics
    db.commit()

    return {
        "summary": summary_text,
        "failed_topics": failed_topics
    }