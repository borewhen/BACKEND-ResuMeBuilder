from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.service.interview_questions import generate_interview_questions_from_skills
from app.models import VideoInterviewSession, VideoInterviewQuestion, VideoInterviewAnswer
from app.schemas import VideoInterviewSessionCreate, VideoInterviewSessionOut, VideoInterviewQuestionCreate, VideoInterviewQuestionOut, VideoInterviewAnswerCreate, VideoInterviewAnswerOut
from app.database import get_db
from typing import List

router = APIRouter()

# 1. Create a new interview session
@router.post("/session/", response_model=VideoInterviewSessionOut)
def create_session(session_data: VideoInterviewSessionCreate, db: Session = Depends(get_db)):
    session = VideoInterviewSession(**session_data.dict())
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


# 2. Get all interview sessions
@router.get("/sessions/", response_model=List[VideoInterviewSessionOut])
def get_sessions(db: Session = Depends(get_db)):
    return db.query(VideoInterviewSession).all()


# 3. Generate interview questions based on resume data (skills)
@router.post("/generate-interview-questions/")
async def generate_interview_questions(resume_data: dict, db: Session = Depends(get_db)):
    """
    1) Accept JSON data extracted from a resume (e.g., skills, experience).
    2) Call the AI service to generate interview questions based on the skills.
    3) Return the generated questions.
    """
    skills = resume_data.get("skills", [])
    if not skills:
        raise HTTPException(status_code=400, detail="No skills found in the resume data.")

    try:
        # Call the AI service to generate questions based on skills
        generated_questions = generate_interview_questions_from_skills(skills)

        # Create and store the generated questions in the session
        # Assuming the session_data contains the session_id (perhaps as part of the resume data)
        session_id = resume_data.get("session_id")  # The session_id should be passed in the request

        if not session_id:
            raise HTTPException(status_code=400, detail="Session ID is required to link questions.")

        # Find the session to link the questions
        session = db.query(VideoInterviewSession).filter(VideoInterviewSession.id == session_id).first()
        if not session:
            raise HTTPException(status_code=404, detail="Session not found.")

        # Store each generated question and link to the session
        for question_text in generated_questions:
            question = VideoInterviewQuestion(text=question_text, session_id=session.id)
            db.add(question)

        db.commit()  # Commit all questions
        db.refresh(session)  # Refresh session to include questions

        return {"questions": generated_questions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating questions: {str(e)}")


# 4. Create a new interview question
@router.post("/question/", response_model=VideoInterviewQuestionOut)
def create_question(question_data: VideoInterviewQuestionCreate, db: Session = Depends(get_db)):
    question = VideoInterviewQuestion(**question_data.dict())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


# 5. Create a new answer
@router.post("/answer/", response_model=VideoInterviewAnswerOut)
def create_answer(answer_data: VideoInterviewAnswerCreate, db: Session = Depends(get_db)):
    answer = VideoInterviewAnswer(**answer_data.dict())
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer
