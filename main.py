from fastapi import FastAPI, Depends, HTTPException, Response
from database import engine, Base, SessionLocal
from crud import create_short_url, get_short_url, update_short_url, delete_short_url, get_url_stats
from schemas import URLCreate, URLResponse, URLStatsResponse
from sqlalchemy.orm import Session


# Creating table(s) and app instance
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


# Retrieve original URL
@app.get("/shorten/{short_code}", response_model=URLResponse, status_code=200)
def get_url(short_code: str, db: Session = Depends(get_db)):
    result = get_short_url(db, short_code)
    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return result


# Update an existing short URL
@app.put("/shorten/{short_code}", response_model=URLResponse, status_code=200)
def update_url(short_code: str, request: URLCreate, db: Session = Depends(get_db)):
    result = update_short_url(db, short_code, request.url)
    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return result


# Delete an existing short URL
@app.delete("/shorten/{short_code}", status_code=204)
def delete_url(short_code: str, db: Session = Depends(get_db)):
    result = delete_short_url(db, short_code)
    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return Response(status_code=204)


# Get URL statistics
@app.get("/shorten/{short_code}/stats", response_model=URLStatsResponse, status_code=200)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    result = get_url_stats(db, short_code)
    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return result
