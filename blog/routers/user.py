from fastapi import APIRouter
from ..import database , schemas ,models
from fastapi import APIRouter, Depends , status , HTTPException
from sqlalchemy.orm import session
from ..hashing import Hash

router = APIRouter
get_db = database.get_db

@router.post('/user', response_model=schemas.ShowUser,tags=["users"])
def user(request: schemas.user, db: Session = Depends(get_db)):
    hashed_password = hashing.Hash.bcrypt(request.password) 
    
    new_user = models.user(
        name=request.name,
        email=request.email,
        password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

