from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class VideoInterviewQuestion(Base):
    __tablename__ = "video_interview_questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=True)
    follow_up = Column(Integer, ForeignKey("video_interview_questions.id"), nullable=True)
    order = Column(Float)  # 0, 1, 2 for main, 0.1, 1.1 for follow-ups
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="video_interview_questions")
