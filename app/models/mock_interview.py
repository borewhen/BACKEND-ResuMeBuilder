from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class MockInterview(Base):
    __tablename__ = "mock_interview"
    __table_args__ = (
        UniqueConstraint('job_id', 'user_id', name='uix_job_user'),
    )

    mock_interview_id = Column(Integer, primary_key=True, index=True)
    job_id = Column(BigInteger, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    company_name =  Column(String, nullable=False)
    job_position =  Column(String, nullable=False)
    summary = Column(Text, nullable=True)
    failed_topics = Column(Text, nullable=True)

    user = relationship("User", back_populates="mock_interviews")
    categories = relationship("Category", back_populates="mock_interview", cascade="all, delete-orphan")
    course = relationship("Course", uselist=False, back_populates="mock_interview")

    def __repr__(self):
        return {
            "mock_interview_id": self.mock_interview_id,
            "job_id": self.job_id,
            "user_id": self.user_id,
            "company_name": self.company_name,
            "job_position": self.job_position,
            "summary": self.summary,
            "failed_topics": self.failed_topics
        }