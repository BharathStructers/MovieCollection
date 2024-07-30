from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    genre = Column(String)
    release_date = Column(String)
    description = Column(String, nullable=True)
    rating = Column(Integer, nullable=True)






# from config.database import Base
# from sqlalchemy import Column,String,TIMESTAMP,Text,Integer
# import uuid


# class Movie(Base):
#   __tablename__ = "movie"
#   id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
#   title = Column(String, nullable=False)
#   director = Column(String, nullable=True)
#   genre = Column(String, nullable=True)
#   release_date = Column(TIMESTAMP(timezone=True), nullable=True)
#   description = Column(Text, nullable=True)
#   rating = Column(Integer, nullable=True)