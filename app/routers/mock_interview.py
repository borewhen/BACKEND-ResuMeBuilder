from fastapi import APIRouter, Depends, HTTPException, Query, Path
from app.models import User
from app.service.user_service import jwt_required
from app.service.job_service import scrape_jobs_list, scrape_job_detail
from typing import List, Dict
from typing import Annotated
from fastapi.exceptions import ResponseValidationError

router = APIRouter()

@router("/")
def generate_interview_topics():
    pass