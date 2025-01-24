from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base
from date import date

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    profile_picture_url = Column(String)
    summary = Column(Text)
    created_at = Column(Date, default=date.utcnow)

    experiences = relationship("Experience", back_populates="user")
    job_applications = relationship("JobApplication", back_populates="user")


class Experience(Base):
    __tablename__ = "experiences"

    experience_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    location = Column(String)
    start_date = Column(date)
    end_date = Column(date)
    description = Column(Text)

    user = relationship("User", back_populates="experiences")


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    website_url = Column(String)
    industry = Column(String)
    logo_url = Column(String)

    jobs = relationship("Job", back_populates="company")


class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))
    title = Column(String, nullable=False)
    description = Column(Text)
    experience_level = Column(String)
    location = Column(String)

    company = relationship("Company", back_populates="jobs")
    job_applications = relationship("JobApplication", back_populates="job")


class JobApplication(Base):
    __tablename__ = "job_applications"

    job_application_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    job_id = Column(Integer, ForeignKey("jobs.job_id"))

    user = relationship("User", back_populates="job_applications")
    job = relationship("Job", back_populates="job_applications")
