from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.database.session import engine
from app.database.base import Base


app = FastAPI(
    title="ScholarTrack API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


app.include_router(health_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "ScholarTrack backend running"}
