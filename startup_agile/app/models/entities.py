from sqlalchemy import Column, Integer, String, Text
from app.models.database import Base

class ResumeMatch(Base):
    __tablename__ = "resume_matches"

    id = Column(Integer, primary_key=True, index=True)
    resume = Column(Text)
    job_description = Column(Text)
    score = Column(Integer)
    feedback = Column(Text)
    photo_check = Column(Text, nullable=True)
    image_base64 = Column(Text, nullable=True)
