from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    lecture_halls = relationship('LectureHall', backref='school')

class LectureHall(Base):
    __tablename__ = 'lecture_halls'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    school_id = Column(Integer(), ForeignKey('schools.id'))
    lectures = relationship('Lecture', back_populates='lecture_hall')
    school = relationship('School', back_populates='lecture_halls')

class Lecture(Base):
    __tablename__ = 'lectures'
    id = Column(Integer(), primary_key=True)
    unit_name = Column(String(), nullable=False)
    start_time = Column(DateTime())
    end_time = Column(DateTime())
    lecture_hall_id = Column(Integer(), ForeignKey('lecture_halls.id'))
    lecture_hall = relationship('LectureHall', back_populates='lectures')

engine = create_engine('sqlite:///lecture_hall.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()














    


