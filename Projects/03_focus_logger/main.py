from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subjects/", response_model=schemas.SubjectResponse)
def create_subject(request: schemas.SubjectCreate, db: Session = Depends(get_db)):
    # FIX 1: We use models.Subject (the database table), not SubjectCreate
    new_subject = models.Subject(title=request.title, is_active=request.is_active)
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    # FIX 2: You must return the object so FastAPI can send it back to the user
    return new_subject 

# FIX 3: Removed the extra '(' before list
@app.get("/subjects/", response_model=list[schemas.SubjectResponse])
def get_all_subjects(db: Session = Depends(get_db)):
    # FIX 4: We query the actual table (models.Subject), not a function name
    subjects = db.query(models.Subject).all()
    return subjects