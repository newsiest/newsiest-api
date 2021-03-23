import os
from sqlalchemy import create_engine, event, DDL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

DB_URL = os.getenv("DB_URL")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_URL = "postgresql://postgres:postgres@localhost/newsiest-db"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_db():
    # with engine.connect() as connection:
    #     connection.execute(text("CREATE SCHEMA IF NOT EXISTS news"))
    # Base.metadata.create_all(bind=engine)
    pass