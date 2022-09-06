from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from src.session_db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'userdata'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=True)
    address = Column(String(50), nullable=True)
    phone = Column(String(20), nullable=True)


Base.metadata.create_all(engine)
Base.metadata.bind = engine

