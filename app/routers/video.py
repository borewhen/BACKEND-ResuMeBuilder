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
        # Call service to process video
        video_path = f"uploads/{file.filename}"
        with open(video_path, "wb") as video_file:
            video_file.write(await file.read())
        
        # Process the video (extract audio, run transcription and analysis)
        process_video(video_path)

        return VideoUploadResponse(success=True, message="Video uploaded and processed successfully.")
    except Exception as e:
        return VideoUploadResponse(success=False, message=str(e))
