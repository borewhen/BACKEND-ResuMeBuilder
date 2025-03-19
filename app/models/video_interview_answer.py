from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class VideoInterviewAnswer(Base):
    __tablename__ = "video_interview_answer"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("video_interview_session.id", ondelete="CASCADE"))
    question_id = Column(Integer, ForeignKey("video_interview_question.id", ondelete="CASCADE"))
    answer_text = Column(Text)
    video_url = Column(Text)
    duration_seconds = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())

    session = relationship("VideoInterviewSession", back_populates="answers")
    question = relationship("VideoInterviewQuestion", back_populates="answers")

