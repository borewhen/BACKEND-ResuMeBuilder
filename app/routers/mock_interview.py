from fastapi import APIRouter, Depends, HTTPException, Query, Path
import os
from app.models import User
from app.service.user_service import jwt_required
from sqlalchemy.orm import Session
from app.service.job_service import get_job_skills_required
from app.database import get_db
from typing import Annotated

router = APIRouter()

OPEN_AI_API_KEY = os.getenv("OPEN_API_KEY", "")

@router.get("/{job_id}")
def generate_interview_topics(job_id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    try:
        skills = get_job_skills_required(job_id)

        return "success", 200
    except Exception:
        raise HTTPException(status_code=500)