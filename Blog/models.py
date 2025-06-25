from .database import Base
from sqlalchemy import Column, Integer, String


class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)  # password is hashed
