from fastapi import APIRouter, Depends, HTTPException, Query, Path
import os
from app.models import User
from app.service.user_service import jwt_required
from sqlalchemy.orm import Session
from app.service.job_service import scrape_job_detail, get_job_skills_required, parse_skills_from_job_desc
from app.database import get_db
from typing import Annotated

router = APIRouter()

OPEN_AI_API_KEY = os.getenv("OPEN_API_KEY", "")

@router.get("/{job_id}")
def generate_interview_topics(job_id: Annotated[int, Path(title="The ID of the item to get")], db: Session = Depends(get_db)):
    try:
        job_detail = scrape_job_detail(job_id)
        job_description = job_detail.job_description

        # check if this job has been put in DB or not
        skills = get_job_skills_required(job_id)
        if not skills:
            # parse skills from description using OpenAI
            skills = parse_skills_from_job_desc(job_detail.job_description)

        return "success", 200
    except Exception:
        raise HTTPException(status_code=500)