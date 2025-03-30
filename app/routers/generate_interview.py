'''
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.service.generate_interview_service import handle_resume_upload

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(
    user_id: int = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        file_bytes = await resume.read()
        first_question = handle_resume_upload(user_id, file_bytes, resume.filename, db)
        return {"first_question": first_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {str(e)}")
'''
# app/routers/generate_interview.py
'''
from fastapi import APIRouter, UploadFile, File, Form, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.service.generate_interview_service import handle_resume_upload
from app.service.submit_answer_service import handle_answer

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(
    user_id: int = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_bytes = await resume.read()
    try:
        first_question = handle_resume_upload(user_id, file_bytes, resume.filename, db)
        return {"first_question": first_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {str(e)}")

@router.post("/submit-answer")
def submit_answer(
    user_id: int = Body(...),
    answer: str = Body(...),
    db: Session = Depends(get_db)
):
    try:
        next_question = handle_answer(user_id, answer, db)
        return {"next_question": next_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get next question: {str(e)}")
'''
# app/routers/generate_interview.py

from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.service.generate_interview_service import handle_resume_upload
from app.service.submit_answer_service import handle_answer
from pydantic import BaseModel


router = APIRouter()

# Upload resume and generate first question
@router.post("/upload-resume")
async def upload_resume(
    user_id: int = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    file_bytes = await resume.read()
    try:
        first_question = handle_resume_upload(user_id, file_bytes, resume.filename, db)
        return {"first_question": first_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {str(e)}")
    
class SubmitAnswerRequest(BaseModel):
    user_id: int
    answer: str 

# Submit an answer (as raw string) and get the next/follow-up question
@router.post("/submit-answer")
def submit_answer(
    body: SubmitAnswerRequest,
    db: Session = Depends(get_db)
):
    try:
        # You get both fields here
        next_question = handle_answer(user_id=body.user_id, answer=body.answer, db=db)
        return {"next_question": next_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get next question: {str(e)}")
