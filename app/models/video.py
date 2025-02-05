from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Video(Base):
    __tablename__ = 'videos'
    
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)  # The name of the video file
    file_path = Column(String)  # The location of the video file
    duration = Column(Integer)  # Video duration in seconds
    format = Column(String)  # Video format (e.g., mp4, avi, etc.)
    uploaded_by = Column(Integer, ForeignKey("users.id"))  # Assuming you have a users table
    
    # Relationship to the User table (if you have a User model)
    user = relationship("User", back_populates="videos")

    def __repr__(self):
        return f"<Video(id={self.id}, file_name={self.file_name}, format={self.format})>"
