from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users_resume import UsersResume
from app.service.generate_interview_service import handle_resume_upload,handle_answer,get_unanswered_question


router = APIRouter()

class SubmitAnswerRequest(BaseModel):
    user_id: int
    answer: str

class QuestionRequest(BaseModel):
    user_id: int

'''
@router.post("/upload-resume")
async def upload_resume(
    user_id: int = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        if not resume.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        file_bytes = await resume.read()
        handle_resume_upload(user_id, file_bytes, resume.filename, db)
        return {"message": "Resume processed and first question stored."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
'''
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
        question = get_unanswered_question(payload.user_id, db)
        return {"question": question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving question: {str(e)}")


@router.post("/submit-answer")
async def submit_answer(payload: SubmitAnswerRequest, db: Session = Depends(get_db)):
    try:
        handle_answer(user_id=payload.user_id, answer=payload.answer, db=db)
        return {"message": "Answer saved and next question generated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Answer submission failed: {str(e)}")
    
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
'''
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
'''