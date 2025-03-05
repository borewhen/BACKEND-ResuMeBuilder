from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Job
from app.schemas.job import JobOut, JobCreate
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required

router = APIRouter()

@router.post("/create", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db), user: User = Depends(jwt_required)):
    new_job = Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/list")
def list_jobs(db: Session = Depends(get_db), user: User = Depends(jwt_required)):
    return db.query(Job).all()
