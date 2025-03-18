from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Course(Base):
    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True, index=True)
    mock_interview_id = Column(Integer, ForeignKey("mock_interview.mock_interview_id"), nullable=False)
    mock_interview = relationship("MockInterview", uselist=False, back_populates="course")
    subtopics = relationship("CourseSubtopic", back_populates="course")