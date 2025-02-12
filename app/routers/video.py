from fastapi import APIRouter, File, UploadFile
from app.service.video_service import process_video
from pydantic import BaseModel

router = APIRouter()

class VideoUploadResponse(BaseModel):
    success: bool
    message: str

@router.post("/upload_video/", response_model=VideoUploadResponse)
async def upload_video(file: UploadFile = File(...)):
    try:
        # Read file content into memory
        video_bytes = await file.read()
        
        # Process the video (extract audio, run transcription and analysis) directly from bytes
        process_video(video_bytes)

        return VideoUploadResponse(success=True, message="Video uploaded and processed successfully.")
    except Exception as e:
        return VideoUploadResponse(success=False, message=str(e))
