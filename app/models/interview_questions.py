from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    interview_question_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    questions = Column(Text, nullable=False)

    user = relationship("User", back_populates="interview_questions")