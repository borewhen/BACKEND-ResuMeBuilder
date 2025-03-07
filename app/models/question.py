from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Question(Base):
    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True, index=True)
    question_name = Column(String, nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategory.subcategory_id"), nullable=False)

    subcategory = relationship("Subcategory", back_populates="questions")
    answer = relationship("Answer", uselist=False, back_populates="question", cascade="all, delete-orphan")