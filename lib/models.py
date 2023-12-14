from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean,UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base= declarative_base()

class LectureHall(Base):
    __tablename__='lecture_halls'

    __table_args__=(
        UniqueConstraint('name', name='uq_lecture_hall_name'),
        PrimaryKeyConstraint('id', name='pk_lecture_hall_id'))

    id = Column(Integer(), primary_key=True)
    name= Column(String(), unique=True, nullable= False)
    status=Column(Boolean(), default= False)
    last_used=Column(DateTime())

    if __name__== '__main__':
        engine= create_engine('sqlite:///lecture_hall.db')
        Base.metadata.create_all(engine)






    


