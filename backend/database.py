# database.py
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "sqlite:///./quiz.db" 

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True, nullable=False)
    title = Column(String, nullable=True)
    date_generated = Column(DateTime, default=datetime.utcnow)
    scraped_content = Column(Text, nullable=True)
    full_quiz_data = Column(Text, nullable=True)

def init_db():
    Base.metadata.create_all(bind=engine)
