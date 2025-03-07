from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Answer(Base):
    __tablename__ = "answer"

    answer_id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    recommended_answer = Column(String, nullable=False)
    
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    question = relationship("Question", back_populates="answer")