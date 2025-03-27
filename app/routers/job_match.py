# app/routers/job_match.py

from fastapi import APIRouter, HTTPException, Body
from app.service.job_matching_service import match_jobs

router = APIRouter()

@router.post("/match")
async def match_jobs_endpoint(resume_data: dict = Body(...)):
    """
    Given a JSON payload containing the extracted resume details,
    return the top matching jobs from the database.
    
    Expected resume_data format example:
    {
       "education": ["B.Sc. in Computer Science"],
       "workExperience": ["Software Engineer at ABC Corp (2019-2022)"],
       "skills": ["Python", "Machine Learning"],
       "certifications": ["AWS Certified Solutions Architect"],
       "hobbies": ["Reading", "Chess"]
    }
    """
    try:
        matches = match_jobs(resume_data)
        return {"matches": matches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error matching jobs: {str(e)}")
