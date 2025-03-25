# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class VideoInterviewSession(Base):
    __tablename__ = "video_interview_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Name or title of the session
    created_at = Column(String)  # Timestamp of session creation

    # Link to questions and answers
    questions = relationship("VideoInterviewQuestion", back_populates="session")
    answers = relationship("VideoInterviewAnswer", back_populates="session")


class VideoInterviewQuestion(Base):
    __tablename__ = "video_interview_questions"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)  # The interview question text
    session_id = Column(Integer, ForeignKey('video_interview_sessions.id'))

    # Relationship with session and answers
    session = relationship("VideoInterviewSession", back_populates="questions")
    answers = relationship("VideoInterviewAnswer", back_populates="question")


class VideoInterviewAnswer(Base):
    __tablename__ = "video_interview_answers"
    
    id = Column(Integer, primary_key=True, index=True)
    answer_text = Column(String)  # The user's answer to the question
    question_id = Column(Integer, ForeignKey('video_interview_questions.id'))
    session_id = Column(Integer, ForeignKey('video_interview_sessions.id'))

    # Relationships to the question and session
    question = relationship("VideoInterviewQuestion", back_populates="answers")
    session = relationship("VideoInterviewSession", back_populates="answers")
