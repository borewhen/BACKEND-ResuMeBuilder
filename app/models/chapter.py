from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Chapter(Base):
    __tablename__ = "chapter"

    chapter_id = Column(Integer, primary_key=True, index=True)
    chapter_name = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey("unit.unit_id"), nullable=False)
    video_thumbnail = Column(String, nullable=True)
    video_title = Column(String, nullable=True)
    video_transcript = Column(Text, nullable=True)
    video_id = Column(String, nullable=True)

    unit = relationship("Unit", back_populates="chapters")

    def to_dict(self):
        """Serialize the Chapter object into a dictionary."""
        return {
            "chapter_id": self.chapter_id,
            "chapter_name": self.chapter_name,
            "video_thumbnail": self.video_thumbnail,
            "video_title": self.video_title,
            "video_transcript": self.video_transcript
        }