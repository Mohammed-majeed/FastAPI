from .database import Base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, text

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, nullable= False)
    name = Column(String, nullable= False)
    email = Column(String, nullable= False, unique= True)
    password = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


# Example model
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String)
    publish = Column(Boolean, nullable= False, default=True)
    rating = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

