from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Experience(Base):
    __tablename__ = "experiences"

    experience_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(Text)

    user = relationship("User", back_populates="experiences")
