from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class Unit(Base):
    __tablename__ = "unit"

    unit_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)
    unit_name = Column(String, nullable=False)

    course = relationship("Course", back_populates="units")
    chapters = relationship("Chapter", back_populates="unit", cascade="all, delete-orphan")

    def to_dict(self):
        """Serialize the Unit object into a dictionary."""
        return {
            "unit_id": self.unit_id,
            "course_id": self.course_id,
            "unit_name": self.unit_name,
            "chapters": [chapter.to_dict() for chapter in self.chapters]
        }