from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    experience_level = Column(String)
    location = Column(String)
    date_of_listing = Column(Date, default=date.today)

    company = relationship("Company", back_populates="jobs")
    job_applications = relationship("JobApplication", back_populates="job")
