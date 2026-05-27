from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class URLInput(BaseModel):
    url: str

@router.post("/check-url")
def check_url(data: URLInput):

    url = data.url.lower()

    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "free",
        "bonus",
        "job",
        "offer",
        "earn"
    ]

    score = 0
    found = []

    for word in suspicious_words:
        if word in url:
            score += 10
            found.append(word)

    if ".xyz" in url or ".tk" in url:
        score += 30

    if score >= 30:
        status = "Suspicious"
    else:
        status = "Safe"

    return {
        "status": status,
        "risk_score": score,
        "matched_keywords": found
    }