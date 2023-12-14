from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean,UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import DateTime

Base= declarative_base()

class School(Base):
    __tablename__='schools'
    id=Column(Integer(), primary_key=True)
    name=Column(String(), nullable=False)
    lecture_halls=relationship('LectureHall',back_populates='school')

class LectureHall(Base):
    __tablename__='lecture_halls'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), unique=True, nullable= False)
    status=Column(Boolean(), default= False)
    last_used=Column(DateTime())

    if __name__== '__main__':
        engine= create_engine('sqlite:///lecture_hall.db')
        Base.metadata.create_all(engine)

        Session=sessionmaker(bind=engine)
        session=Session()






    


