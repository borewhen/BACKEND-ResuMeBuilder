from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    profile_picture_url = Column(String)
    summary = Column(Text)
    role = Column(String, nullable=False)  # Possible values: 'employer', 'employee', 'admin'
    created_at = Column(Date, default=date.today)

    mock_interviews = relationship("MockInterview", back_populates="user", cascade="all, delete-orphan")
    courses = relationship("Course", back_populates="user", cascade="all, delete-orphan")
    users_resume = relationship("UsersResume", back_populates="user", uselist=False)
    video_interview_questions = relationship("VideoInterviewQuestion", back_populates="user", cascade="all, delete-orphan")


