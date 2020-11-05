from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from smart_env import ENV

if ENV.TEST:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/test_task"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


