from fastapi import APIRouter, Depends, HTTPException, Path, File, UploadFile
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required
from app.service.mock_interview_service import create_mock_interview, parse_skills_from_job, get_mock_interview_topics, get_existing_interview_session_info, initialize_subcategory_interview_session, update_answer, get_user_questions, generate_subcategory_summary, generate_mock_interview_summary
from app.schemas.answer import AnswerRequest

router = APIRouter()

@router.post("/{job_id}")
def generate_interview_topics(
    job_id: Annotated[int, Path(title="The ID of the job")], 
    db: Session = Depends(get_db), 
    user: User = Depends(jwt_required)
):
    try:
        mock_interview, is_exist = create_mock_interview(db, job_id, user.user_id)
        if not is_exist:
            parse_skills_from_job(db, job_id, mock_interview.mock_interview_id)
            mock_interview = get_mock_interview_topics(db, job_id, user.user_id)
        db.commit()
        return mock_interview
    except Exception as e:
        print(str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/session/{subcategory_id}")
def get_interview_data(
    subcategory_id: Annotated[int, Path(title="The ID of the subcategory")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    # get the current interview session
    return get_existing_interview_session_info(db, user.user_id, subcategory_id)


@router.post("/session/{subcategory_id}")
def create_first_interview_question(
    subcategory_id: Annotated[int, Path(title="The ID of the subcategory")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
): 
    # creates first interview question 
    initialize_subcategory_interview_session(db, subcategory_id, user.user_id)
    return {"message": "interview session started"}


@router.put("/session/{subcategory_id}")
def answer_interview_questions(
    subcategory_id: Annotated[int, Path(title="The ID of the subcategory")],
    answer_data: AnswerRequest,
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required),
):
    """
    Receives an answer from the user and updates the interview session.
    """
    update_answer(db, user.user_id, subcategory_id, answer_data.answer)
    return {"message": "Answer received successfully"}


@router.get("/{subcategory_id}/summary")
def create_subcategory_summary(
    subcategory_id: Annotated[int, Path(title="The ID of the subcategory")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required),
):
    """
    Generating summary per subcategory, only if status is false
    """
    summary = generate_subcategory_summary(db, subcategory_id, user.user_id)
    return { "summary": summary }


@router.get("/summary/{job_id}")
def create_summary(
    job_id: Annotated[int, Path(title="The ID of the job")], 
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required),
):
    """
    Generate summary per mock interview, only if all subcategory has been done
    """
    result = generate_mock_interview_summary(db, job_id, user.user_id)
    return result