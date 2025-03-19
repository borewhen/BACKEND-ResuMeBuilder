from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class VideoInterviewQuestion(Base):
    __tablename__ = "video_interview_question"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("video_interview_session.id", ondelete="CASCADE"))
    question_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    session = relationship("VideoInterviewSession", back_populates="questions")
    answers = relationship("VideoInterviewAnswer", back_populates="question")
