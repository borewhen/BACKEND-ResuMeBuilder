from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    mock_interview_id = Column(Integer,  ForeignKey("mock_interview.mock_interview_id"), nullable=False)
    category_name = Column(String, nullable=False)

    mock_interview = relationship("MockInterview", back_populates="categories")
    subcategories = relationship("Subcategory", back_populates="category", cascade="all, delete-orphan")
