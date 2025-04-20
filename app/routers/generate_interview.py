from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users_resume import UsersResume
from app.service.generate_interview_service import handle_resume_upload,handle_answer,get_interview_data, handle_finish_interview, generate_video_interview_summary
from typing import List

router = APIRouter()

class SubmitAnswerRequest(BaseModel):
    user_id: int
    answer: str
    summary: str

class QuestionRequest(BaseModel):
    user_id: int

class InterviewItem(BaseModel):
    question: str
    answer: str

class Interview(BaseModel):
    questions: List[str]
    answers: List[str]
    feedbacks: List[str]

class FinishInterviewRequest(BaseModel):
    user_id: int
    summary: str
    interview: Interview
    
@router.post("/start-interview")
async def start_interview(
    user_id: int = Form(...),
    resume: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    try:
        file_bytes = await resume.read() if resume else None
        filename = resume.filename if resume else None
        question = handle_resume_upload(user_id, file_bytes, filename, db)
        return {"status": "Resume processed and question generated successfully."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")

@router.post("/get-question")
async def get_question(payload: QuestionRequest, db: Session = Depends(get_db)):
    try:
        return get_interview_data(payload.user_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving question: {str(e)}")


@router.post("/submit-answer")
async def submit_answer(payload: SubmitAnswerRequest, db: Session = Depends(get_db)):
    try:
        handle_answer(user_id=payload.user_id, answer=payload.answer, summary=payload.summary, db=db)
        return {"message": "Answer saved and next question generated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Answer submission failed: {str(e)}")

@router.post("/finish-interview")
async def finish_interview(payload: FinishInterviewRequest, db: Session = Depends(get_db)):
    try:
        feedback = generate_video_interview_summary(payload, db=db)
        handle_finish_interview(user_id=payload.user_id, db=db)
        return feedback
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error finishing interview: {str(e)}")