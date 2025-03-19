from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required

router = APIRouter()

@router.post("")
def generate_course(
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    """
    get list of courses of the user
    """
    pass


@router.post("/{course_id}")
def generate_course(
    mock_interview_id: Annotated[int, Path(title="The ID of the mock interview session")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    pass


@router.post("/{mock_interview_id}")
def generate_course(
    mock_interview_id: Annotated[int, Path(title="The ID of the mock interview session")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    pass


@router.post("/{mock_interview_id}")
def generate_course(
    mock_interview_id: Annotated[int, Path(title="The ID of the mock interview session")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    pass