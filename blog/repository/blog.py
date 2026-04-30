from sqlalchemy.orm import Session
from .. import models , database 

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create():
    new_blog = models.Blog(title=request.title , body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog