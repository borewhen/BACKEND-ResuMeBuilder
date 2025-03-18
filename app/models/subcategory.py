from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Subcategory(Base):
    __tablename__ = "subcategory"

    subcategory_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer,  ForeignKey("category.category_id"), nullable=False)
    subcategory_name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    summary = Column(String)

    category = relationship("Category", back_populates="subcategories")
    questions = relationship("Question", back_populates="subcategory", cascade="all, delete-orphan")