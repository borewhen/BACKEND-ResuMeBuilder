from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required
from app.service.course_service import get_all_courses, get_course_by_id, create_course, create_course_video
from app.schemas.course import CourseCreateRequest

router = APIRouter()

@router.get("")
def get_course(
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    """
    get list of courses of the user
    """
    courses = get_all_courses(db, user.user_id)
    return courses


@router.get("/{course_id}")
def get_course_detail(
    course_id: Annotated[int, Path(title="The ID of course")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    """
    get course detail
    """
    course = get_course_by_id(db, course_id, user.user_id)
    return course


@router.post("/{mock_interview_id}")
def generate_course(
    mock_interview_id: Annotated[int, Path(title="The ID of the mock interview session")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    """
    create new course based on this mock interview
    """
    course = create_course(db, mock_interview_id, user.user_id)
    return {"message": "course created successfully", "course_id": course.course_id}


@router.put("/{course_id}")
def update_course_video(
    course_id: Annotated[int, Path(title="The ID of the course")],
    db: Session = Depends(get_db),
    user: User = Depends(jwt_required)
):
    """
    generate course video
    """
    create_course_video(db, course_id)
    return {"message": "course content generated successfully"}