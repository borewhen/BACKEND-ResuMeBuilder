from fastapi import APIRouter, Depends, HTTPException, Query, Path
import os
from app.models import User
from app.service.user_service import jwt_required
from app.service.job_service import scrape_jobs_list, scrape_job_detail
from typing import List, Dict
from typing import Annotated
from fastapi.exceptions import ResponseValidationError

router = APIRouter()

OPEN_AI_API_KEY = os.getenv("OPEN_API_KEY", "")

@router.get("/{job_id}")
def generate_interview_topics(job_id: Annotated[int, Path(title="The ID of the item to get")]):
    pass