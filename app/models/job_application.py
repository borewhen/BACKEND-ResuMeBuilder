from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class JobApplication(Base):
    __tablename__ = "job_applications"

    job_application_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    job_id = Column(Integer, ForeignKey("jobs.job_id"))
    date_of_application = Column(Date, default=date.today)

    user = relationship("User", back_populates="job_applications")
    job = relationship("Job", back_populates="job_applications")