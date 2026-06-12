from fastapi import FastAPI, Depends, HTTPException
from database import engine, Base, SessionLocal
from crud import create_short_url, get_short_url, update_short_url, delete_short_url, get_url_stats
from schemas import URLCreate, URLResponse, URLStatsResponse
from sqlalchemy.orm import Session


# Creating table(s) and app isntance
Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency injection to create a session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a new short URL
@app.post("/shorten", response_model=URLResponse, status_code=201)
def create_url(request: URLCreate, db: Session = Depends(get_db)):
    return create_short_url(db, request.url)
