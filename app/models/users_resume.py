# app/models/users_resume.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from app.database import Base

class UsersResume(Base):
    __tablename__ = "users_resume"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    resume_extracted = Column(JSON, nullable=True)
    pdf_link = Column(String, nullable=True)

    user = relationship("User", back_populates="users_resume")
