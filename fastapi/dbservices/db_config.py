import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# load_dotenv()
# SQLALCHEMY_DATABASE_URL = os.getenv(SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:anshi@localhost:5432/abc"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db( ):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def create_table():
    Base.metadata.create_all(bind=engine)   

