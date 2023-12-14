from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base= declarative_base()

class LectureHall(Base):
    __tablename__='lecture_halls'


    id = Column(Integer(), primary_key=True)
    name= Column(String(), unique=True, nullable= False)
    status=Column(Boolean(), default= False)
    last_used=Column(DateTime())


