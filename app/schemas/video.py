from pydantic import BaseModel
from typing import Optional

class VideoBase(BaseModel):
    file_name: str  # Name of the video file
    file_path: str  # Path where the video is stored
    duration: Optional[int] = None  # Duration in seconds, optional
    format: str  # Video format (e.g., mp4, avi, etc.)

    class Config:
        orm_mode = True  # Tells Pydantic to treat the ORM model as a dict

class VideoCreate(VideoBase):
    pass  # You can add additional fields if needed for video creation

class VideoOut(VideoBase):
    id: int  # Include ID when returning video data

    class Config:
        orm_mode = True
