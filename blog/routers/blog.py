from fastapi import APIRouter, Depends , status
from typing import List
from .. import schemas, database, models
from sqlalchemy.orm import Session 

router = APIRouter()

@router.post('/blog',status_code=status.HTTP_201_CREATED,tags=["blogs"])
def create(request:schemas.Blog ,db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title , body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=["blogs"])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs