from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

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