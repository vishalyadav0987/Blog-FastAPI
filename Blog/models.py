from .database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User',back_populates='blogs')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)  # password is hashed
    blogs = relationship('Blog', back_populates='user')  # back_populates is used
