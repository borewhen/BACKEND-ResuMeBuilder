import uuid
import json
import boto3
from app.service.resume_extraction_service import parse_resume_pdf_bytes
from sqlalchemy.orm import Session
from app.models.users_resume import UsersResume
from app.models.video_interview_questions import VideoInterviewQuestion
import openai

# ---- HARDCODED CONFIG ----
AWS_ACCESS_KEY_ID = "AKIAXYS5JEWLWJKU6PPS"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "ap-southeast-2"  
S3_BUCKET_NAME = "resume-storagedip"
openai.api_key = "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"  # Or read from env in production


# --- S3 Upload Function ---
s3_client = boto3.client("s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_to_s3(file_bytes: bytes, filename: str) -> str:
    s3_key = f"resumes/{uuid.uuid4()}_{filename}"
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=s3_key, Body=file_bytes, ContentType="application/pdf")
    return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{s3_key}"


def handle_resume_upload(user_id: int, file_bytes: bytes | None, filename: str | None, db: Session) -> str:
    # 1. Use uploaded resume if available
    if file_bytes:
        s3_url = upload_to_s3(file_bytes, filename)
        resume_json = parse_resume_pdf_bytes(file_bytes)

        existing = db.query(UsersResume).filter_by(user_id=user_id).first()
        if existing:
            existing.resume_extracted = resume_json
            existing.pdf_link = s3_url
        else:
            db.add(UsersResume(user_id=user_id, resume_extracted=resume_json, pdf_link=s3_url))
        db.commit()
    else:
        # No new upload, check existing
        existing = db.query(UsersResume).filter_by(user_id=user_id).first()
        if not existing:
            raise ValueError("No resume uploaded and no existing resume found in the system.")
        resume_json = existing.resume_extracted

    # 2. Generate first question
    prompt = f"""
    You are a mock interviewer. Based on this resume, generate a first interview question. The question can be technical or behavioral.
    Instructions:
    - Ensure the question is specific to the candidate’s resume — refer to their projects, companies, skills, or experiences.
    - The technical questions should assess their hands-on work with tools, platforms, and problem-solving.
    - The behavioral questions should explore communication, teamwork, initiative, or adaptability based on resume content.
    - Avoid generic or overly vague questions.
    - Use a maximum of 20 words.
    Resume: {json.dumps(resume_json, indent=2)}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=250,
        temperature=0.7
    )
    question_text = response["choices"][0]["message"]["content"].strip()

    # 3. Save question to DB
    db.add(VideoInterviewQuestion(user_id=user_id, question=question_text))
    db.commit()

    return question_text
# --- Get Unanswered Question ---
def get_interview_data(user_id: int, db: Session):
    datas = (db.query(VideoInterviewQuestion)
    .filter_by(user_id=user_id)
    .order_by(VideoInterviewQuestion.id.asc())
    .all())
    
    questions = []
    answers = []
    
    for data in datas:
        questions.append(data.question)
        if data.answer is not None:
            answers.append(data.answer)
    
    return {
        "questions": questions,
        "answers": answers
    }

def handle_answer(user_id: int, answer: str, db: Session) -> None:
    # Get the most recent unanswered question
    prev_q = db.query(VideoInterviewQuestion)\
        .filter_by(user_id=user_id, answer=None)\
        .order_by(VideoInterviewQuestion.id.desc())\
        .first()

    if not prev_q:
        raise ValueError("No active question found.")

    prev_q.answer = answer
    db.commit()

    # Resume data
    resume_data = db.query(UsersResume).filter_by(user_id=user_id).first()
    resume_json = resume_data.resume_extracted if resume_data else {}

    # Generate next/follow-up question
    prompt = f"""
    You are conducting an AI interview.

    Previous question: {prev_q.question}
    Candidate's answer: {answer}

    Resume: {json.dumps(resume_json)}

    If the answer is strong and complete, ask a new interview question(behavorial or technical) about a DIFFERENT project or skill.
    Instructions:
    - Ensure the question is specific to the candidate’s resume — refer to their projects, companies, skills, or experiences.
    - The technical questions should assess their hands-on work with tools, platforms, and problem-solving.
    - The behavioral questions should explore communication, teamwork, initiative, or adaptability based on resume content.
    - Avoid generic or overly vague questions.
    - Use a maximum of 20 words.
    If the answer lacks detail, ask a follow-up question to dive deeper into the previous question.

    Return ONLY the next question text.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )

    next_q = response["choices"][0]["message"]["content"].strip()

    # Save new question
    db.add(VideoInterviewQuestion(user_id=user_id, question=next_q))
    db.commit()

def handle_finish_interview(user_id: int, db: Session) -> None:
    try:
        (db.query(VideoInterviewQuestion)
         .filter_by(user_id=user_id)
         .delete())
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        return {"message": "DB reset successfully"}