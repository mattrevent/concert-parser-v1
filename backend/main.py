from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import Depends

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