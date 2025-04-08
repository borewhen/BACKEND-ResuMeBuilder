from fastapi import APIRouter, Depends, HTTPException, Query, Path
from app.models import User
from app.service.user_service import jwt_required
from app.service.job_service import scrape_jobs_list, scrape_job_detail, format_desc
from typing import List, Dict
from typing import Annotated

router = APIRouter()

@router.get("/")
def list_jobs(
    field: Annotated[str, Query(description="Filter jobs by field (e.g., Software Engineer)")] = None,
    page: Annotated[int, Query(description="Page number for pagination")] = 1,
    user: User = Depends(jwt_required)
):
    """
    Retrieves a list of job postings based on the provided field filter.
    - field: Filter jobs by specific field (company name or job name).
    - page: Page number for paginated results.
    - user: Requires authentication (JWT token).
    """
    try:
        return scrape_jobs_list(field, page)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{job_id}")
def get_job_detail(
    job_id: Annotated[int, Path(title="The ID of the item to get")], 
    user: User = Depends(jwt_required)
):
    """
    Retrieves details of a specific job using job_id.
    - job_id: The unique identifier for the job.
    - user: Requires authentication (JWT token).
    """
    if job_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid job ID")

    try:
        job = scrape_job_detail(job_id)[0]
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        return job
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

@router.get("/{job_id}/description")
def format_job_desc(
    job_id: Annotated[int, Path(title="The ID of the item to get")], 
    user: User = Depends(jwt_required)
):
    """
    Retrieves description of a specific job using job_id.
    - job_id: The unique identifier for the job.
    - user: Requires authentication (JWT token).
    """
    if job_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid job ID")

    try:
        desc = format_desc(job_id)
        if not desc:
            raise HTTPException(status_code=404, detail="Job not found")
        return desc
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")