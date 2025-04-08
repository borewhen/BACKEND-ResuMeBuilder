from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class Course(Base):
    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=True)
    mock_interview_id = Column(Integer, ForeignKey("mock_interview.mock_interview_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    job_position = Column(String, nullable=False)
    company_name = Column(String, nullable=False)

    mock_interview = relationship("MockInterview", uselist=False, back_populates="course")
    units = relationship("Unit", back_populates="course", cascade="all, delete-orphan")
    user = relationship("User", back_populates="courses")

    def to_dict(self):
        """Serialize the Course object into a dictionary."""
        return {
            "course_id": self.course_id,
            "image_url": self.image_url,
            "mock_interview_id": self.mock_interview_id,
            "user_id": self.user_id,
            "job_position": self.job_position,
            "company_name": self.company_name,
            "units": [unit.to_dict() for unit in self.units]
        }
        