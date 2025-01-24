from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    profile_picture_url = Column(String)
    summary = Column(Text)
    role = Column(String, nullable=False)  # Possible values: 'employer', 'employee', 'admin'
    created_at = Column(Date, default=date.today)

    experiences = relationship("Experience", back_populates="user")
    job_applications = relationship("JobApplication", back_populates="user")


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


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    website_url = Column(String)
    industry = Column(String)
    logo_url = Column(String)
    address = Column(String)

    jobs = relationship("Job", back_populates="company")


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


class JobApplication(Base):
    __tablename__ = "job_applications"

    job_application_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    job_id = Column(Integer, ForeignKey("jobs.job_id"))
    date_of_application = Column(Date, default=date.today)

    user = relationship("User", back_populates="job_applications")
    job = relationship("Job", back_populates="job_applications")

