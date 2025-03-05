from sqlalchemy import Column, Integer, String
from app.database import Base

class Skill(Base):
    __tablename__ = "skills"

    skill_id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer)
    skill_name = Column(String, nullable=False)
    skill_category = Column(String, nullable=False)

    def __repr__(self):
        return {
            "skill_id": self.skill_id, 
            "job_id": self.job_id,
            "skill_name": self.skill_name,
            "skill_category": self.skill_category
        }