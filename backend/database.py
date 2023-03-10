from os import environ

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URL'))
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
