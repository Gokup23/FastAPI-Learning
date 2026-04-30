from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from .. import database, schemas, models 
from ..hashing import Hash

def create(request:schemas.user , db: Session):
    hashed_password = Hash.bcrypt(request.password) 
    
    new_user = models.user(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user