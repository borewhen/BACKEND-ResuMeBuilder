from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MockInterview(Base):
    __tablename__ = "mock_interview"

    mock_interview_id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    user = relationship("User", back_populates="mock_interviews")
    categories = relationship("Category", back_populates="mock_interview", cascade="all, delete-orphan")
