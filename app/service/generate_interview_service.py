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

'''
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

def upload_to_s3(file_bytes: bytes, filename: str) -> str:
    s3_key = f"resumes/{uuid.uuid4()}_{filename}"
    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=s3_key,
        Body=file_bytes,
        ContentType="application/pdf"
    )
    return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

def generate_first_question(resume_json: dict) -> str:
    prompt = f"""
    Based on the following resume details, generate the first interview question (either behavioral or technical):
    {json.dumps(resume_json, indent=2)}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )
    return response["choices"][0]["message"]["content"].strip()

def handle_resume_upload(user_id: int, file_bytes: bytes, filename: str, db: Session) -> str:
    # 1. Upload to S3
    s3_url = upload_to_s3(file_bytes, filename)

    # 2. Extract structured info from resume
    resume_json = parse_resume_pdf_bytes(file_bytes)

    # 3. Save to DB
    db_resume = UsersResume(
        user_id=user_id,
        resume_extracted=resume_json,
        pdf_link=s3_url
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)

    # 4. Generate first question
    question = generate_first_question(resume_json)
    return question
'''
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_to_s3(file_bytes: bytes, filename: str) -> str:
    s3_key = f"resumes/{uuid.uuid4()}_{filename}"
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=s3_key, Body=file_bytes, ContentType="application/pdf")
    return f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

def handle_resume_upload(user_id: int, file_bytes: bytes, filename: str, db: Session) -> str:
    s3_url = upload_to_s3(file_bytes, filename)
    resume_json = parse_resume_pdf_bytes(file_bytes)

    db.add(UsersResume(user_id=user_id, resume_extracted=resume_json, pdf_link=s3_url))
    db.commit()

    prompt = f"""
    You are an expert interviewer preparing a mock interview.

    Given the candidate’s resume below, generate **5 personalized interview questions** in alternating order — a mix of **technical and behavioral** questions (e.g., tech, behavioral, tech, behavioral, tech).

    Instructions:
    - Ensure each question is specific to the candidate’s resume — refer to their projects, companies, skills, or experiences.
    - The technical questions should assess their hands-on work with tools, platforms, and problem-solving.
    - The behavioral questions should explore communication, teamwork, initiative, or adaptability based on resume content.
    - Avoid generic or overly vague questions.
    - Number the questions 1 to 5.

    Resume:
    {json.dumps(resume_json, indent=2)}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=600
    )

    lines = response["choices"][0]["message"]["content"].strip().split('\n')
    questions = [line.split('.', 1)[-1].strip() for line in lines if line.strip()]

    for i, q in enumerate(questions):
        db.add(VideoInterviewQuestion(user_id=user_id, question=q, order=float(i)))
    db.commit()

    return questions[0]