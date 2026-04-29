from fastapi import FastAPI, Depends , status, Response
from . import schemas , models , hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import blog

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)

