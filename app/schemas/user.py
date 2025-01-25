from pydantic import BaseModel
from datetime import date
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    role: str
    profile_picture_url: Optional[str] = None
    summary: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    user_id: int
    created_at: date

    class Config:
        from_attributes = True

# Login Schema
class UserLogin(BaseModel):
    email: str
    password: str
