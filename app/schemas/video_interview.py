# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class VideoInterviewSessionCreate(BaseModel):
    name: str
    created_at: str  # You can adjust the type based on your needs, e.g., datetime
    
    class Config:
        orm_mode = True

class VideoInterviewSessionOut(BaseModel):
    id: int
    name: str
    created_at: str
    
    class Config:
        orm_mode = True

class VideoInterviewQuestionCreate(BaseModel):
    text: str
    session_id: int
    
    class Config:
        orm_mode = True

class VideoInterviewQuestionOut(BaseModel):
    id: int
    text: str
    session_id: int
    
    class Config:
        orm_mode = True

class VideoInterviewAnswerCreate(BaseModel):
    answer_text: str
    question_id: int
    session_id: int
    
    class Config:
        orm_mode = True

class VideoInterviewAnswerOut(BaseModel):
    id: int
    answer_text: str
    question_id: int
    session_id: int
    
    class Config:
        orm_mode = True
