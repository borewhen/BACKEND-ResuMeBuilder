from fastapi import APIRouter, File, UploadFile
from app.service.video_service import process_video
from pydantic import BaseModel
from sse_starlette import EventSourceResponse
import logging
import asyncio

router = APIRouter()

class VideoUploadResponse(BaseModel):
    success: bool
    message: str
    transcript: str = None
    analysis: str = None

# Updated to use EventSourceResponse for streaming feedback
@router.post("/upload_video/", response_model=VideoUploadResponse)
async def upload_video(file: UploadFile = File(...)):
    logging.info(f"Uploading video: {file.filename}")

    # Read the file asynchronously
    video_bytes = await file.read()  # Use async read for the file

    # Check if video bytes are empty
    if not video_bytes:
        logging.error(f"Received an empty video file: {file.filename}")
        return VideoUploadResponse(success=False, message="Received empty video file.")
    
    # Log file size and other info
    logging.info(f"Received file: {file.filename}, size: {len(video_bytes)} bytes")

    # Create a feedback generator for streaming
    async def feedback_generator():
        feedback_queue = []

        # Process video synchronously (blocking operation)
        data = await asyncio.to_thread(process_video, video_bytes, feedback_queue)

        # Stream feedback in real-time
        for feedback in feedback_queue:
            yield f"data: {feedback}\n\n"

        # After processing, return final result
        yield f"data: Final result: {data}\n\n"

    # Return EventSourceResponse to stream feedback to the frontend
    return EventSourceResponse(feedback_generator())
