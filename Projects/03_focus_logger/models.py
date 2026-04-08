from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) # e.g., "GATE DA: Machine Learning"
    is_active = Column(Boolean, default=True)

    # This links the Subject to multiple StudySessions
    sessions = relationship("StudySession", back_populates="subject")

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    
    # The ForeignKey points to the exact table name and column ("subjects.id")
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    duration_minutes = Column(Integer)
    notes = Column(String) # e.g., "Practiced OS and shutil modules today"

    # This links the StudySession back to its specific Subject
    subject = relationship("Subject", back_populates="sessions")