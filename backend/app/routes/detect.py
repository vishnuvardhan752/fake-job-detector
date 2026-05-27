from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import JobScan

router = APIRouter()


class JobInput(BaseModel):
    description: str


@router.post("/analyze")
def analyze_job(job: JobInput):

    text = job.description.lower()

    suspicious_keywords = {
        "registration fee": 30,
        "security deposit": 30,
        "urgent hiring": 20,
        "earn money fast": 25,
        "work from home": 15,
        "limited slots": 20,
        "payment required": 30,
        "no experience needed": 20,
        "whatsapp": 15,
        "telegram": 15,
        "guaranteed placement": 25,
        "instant joining": 20,
        "refundable fee": 30,
        "daily earnings": 20,
        "no interview": 25,
        "submit payment": 30,
        "verification fee": 30
    }

    score = 0
    found_keywords = []

    for keyword, points in suspicious_keywords.items():
        if keyword in text:
            score += points
            found_keywords.append(keyword)

    if "₹" in text or "lakh" in text:
        score += 15

    if score >= 40:
        prediction = "Fake"
    else:
        prediction = "Real"

    confidence = min(score + 40, 99)

    db: Session = SessionLocal()

    new_scan = JobScan(
        description=job.description,
        prediction=prediction,
        confidence=confidence,
        risk_score=score
    )

    db.add(new_scan)
    db.commit()
    db.close()

    return {
        "prediction": prediction,
        "confidence": confidence,
        "risk_score": score,
        "suspicious_keywords": found_keywords
    }