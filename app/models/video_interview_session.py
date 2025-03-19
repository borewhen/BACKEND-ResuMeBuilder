from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class VideoInterviewSession(Base):
    __tablename__ = "video_interview_session"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    status = Column(String(50), nullable=False, default="pending")  # pending, completed, failed
    duration_seconds = Column(Integer)
    feedback = Column(Text)

    questions = relationship("VideoInterviewQuestion", back_populates="session")
    answers = relationship("VideoInterviewAnswer", back_populates="session")
    analysis = relationship("VideoInterviewAnalysis", back_populates="session")
