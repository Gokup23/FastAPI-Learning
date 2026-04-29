from fastapi import FastAPI, Depends , status, Response
from . import schemas , models , hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import blog

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router)


@app.post('/user', response_model=schemas.ShowUser,tags=["users"])
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
