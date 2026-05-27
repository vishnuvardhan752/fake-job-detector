from sqlalchemy import Column, Integer, String
from app.database import Base

class JobScan(Base):
    __tablename__ = "job_scans"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    prediction = Column(String)
    confidence = Column(Integer)
    risk_score = Column(Integer)