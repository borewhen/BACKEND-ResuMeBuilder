from fastapi import APIRouter, Depends, HTTPException, Path, File, UploadFile
from sqlalchemy.orm import Session
from typing import Annotated
from app.database import get_db
from app.models import User
from app.service.user_service import jwt_required
from app.service.mock_interview_service import create_mock_interview, parse_skills_from_job, get_transcript

router = APIRouter()

@router.post("/transcript")
async def get_audio_transcript(
    file: UploadFile = File(...),
):
    try:
        # Process the audio file and return the transcript
        transcript = await get_transcript(file)
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{job_id}")
def generate_interview_topics(
    job_id: Annotated[int, Path(title="The ID of the job")], 
    db: Session = Depends(get_db), 
    user: User = Depends(jwt_required)
):
    try:
        mock_interview, is_exist = create_mock_interview(db, job_id, user.user_id)
        if not is_exist:
            mock_interview = parse_skills_from_job(db, job_id, mock_interview.mock_interview_id)
        db.commit()
        return mock_interview
    except Exception as e:
        print(str(e))
        db.rollback()  # Rollback in case of failure
        raise HTTPException(status_code=500, detail=str(e))

