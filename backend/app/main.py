from app.routes.url_checker import router as url_router
from app.routes.dashboard import router as dashboard_router
from app.database import engine
from app.models import Base
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.detect import router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(dashboard_router)
app.include_router(url_router)

@app.get("/")
def home():
    return {"message": "Fake Job Detector API Running"}

