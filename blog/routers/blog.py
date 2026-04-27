from fastapi import APIRouter
from typing import List
from .. import schemas,database , models
router = APIRouter()


@router.get('/blog',response_model=List[schemas.ShowBlog],tags=["blogs"])
def all(db:Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs