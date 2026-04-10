from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#This will create a local file named 'randle_planner.db' right in this folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./randle_planner.db"

#connectargs required for SQlite only 
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()