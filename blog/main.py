from fastapi import FastAPI, Depends , status, Response
from . import schemas , models , hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import blog

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router)



@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")
    blog.update({'title': request.title, 'body': request.body}, synchronize_session=False)
    db.commit()
    return 'updated'

@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=["blogs"])
def show(id,response : Response , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id ==id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { 'detail' : f'blog with the id {id} not found ! '}
    return blog

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
