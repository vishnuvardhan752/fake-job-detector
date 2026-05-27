from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import JobScan

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_data():

    db: Session = SessionLocal()

    total_scans = db.query(JobScan).count()

    fake_jobs = db.query(JobScan).filter(
        JobScan.prediction == "Fake"
    ).count()

    real_jobs = db.query(JobScan).filter(
        JobScan.prediction == "Real"
    ).count()

    db.close()

    return {
        "total_scans": total_scans,
        "fake_jobs": fake_jobs,
        "real_jobs": real_jobs
    }