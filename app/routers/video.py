from fastapi import APIRouter, File, UploadFile
from app.service.video_service import process_video
from pydantic import BaseModel
import time

router = APIRouter()

class VideoUploadResponse(BaseModel):
    success: bool
    message: str
    transcript: str = None
    analysis: str = None

@router.post("/upload_video/", response_model=VideoUploadResponse)
async def upload_video(file: UploadFile = File(...)):
    print(f"Uploading video: {file.filename}")
    try:
        # Read file content into memory
        video_bytes = await file.read()
        
        # Process the video (extract audio, run transcription and analysis) directly from bytes
        data = process_video(video_bytes)

        return VideoUploadResponse(success=True, message="Video uploaded and processed successfully.", transcript=data['transcript'], analysis=data['analysis'])
    except Exception as e:
        return VideoUploadResponse(success=False, message=str(e))
