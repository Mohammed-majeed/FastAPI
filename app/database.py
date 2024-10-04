from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import setting

# Corrected connection string
SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.DATABASE_NAME}:{setting.DATABASE_PASSWORD}@{
    setting.DATABASE_HOSTNAME}:{setting.DATABASE_PORT}/{setting.DATABASE_USERNAME}'


# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()