from sqlalchemy.engine import create_engine
from sqlalchemy.orm import  sessionmaker, DeclarativeBase

DB_URL = 'sqlite:///./house_app.db'
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass