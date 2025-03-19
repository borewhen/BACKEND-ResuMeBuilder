from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Unit(Base):
    __tablename__ = "unit"

    unit_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)

    course = relationship("Course", back_populates="units")
    chapters = relationship("Chapter", back_populates="unit", cascade="all, delete-orphan")