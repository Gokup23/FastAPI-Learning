from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session 
from .. import database, schemas, models 
from ..hashing import Hash 

router = APIRouter(prefix="/user",tags=['users'])

get_db = database.get_db

@router.post('', response_model=schemas.ShowUser, )
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    
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