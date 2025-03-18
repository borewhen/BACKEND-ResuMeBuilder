from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CourseSubtopic(Base):
    __tablename__ = "course_subtopic"

    course_subtopic_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)
    course = relationship("Course", back_populates="subtopics")
