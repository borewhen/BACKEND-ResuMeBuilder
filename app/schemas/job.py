from pydantic import BaseModel
from datetime import date
from typing import Optional

class JobBase(BaseModel):
    title: str
    company_id: int
    description: Optional[str] = None
    experience_level: Optional[str] = None
    location: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    job_id: int
    date_of_listing: date

    class Config:
        from_attributes = True 