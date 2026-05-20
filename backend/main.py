from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from scraper import scrape_kassir

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
def get_status():
    return {"status": "ok"}

@app.get("/api/concerts")
def get_concerts(db: Session = Depends(get_db)):
    concerts = db.query(models.Concert).all()
    return concerts

@app.post("/api/search")
def search_concerts(artist: str, db: Session = Depends(get_db)):
    results = scrape_kassir(artist)

    for item in results:
        concert = models.Concert(**item)
        db.add(concert)

    db.commit()
    return {"status": "ok", "found": len(results)}