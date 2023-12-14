from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import click

Base= declarative_base()

class School(Base):
    __tablename__='schools'
    id=Column(Integer(), primary_key=True)
    name=Column(String(), nullable=False)
    lecture_halls=relationship('LectureHall',backref='school')

class LectureHall(Base):
    __tablename__='lecture_halls'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), unique=True, nullable= False)
    school_id=Column(Integer(), ForeignKey('schools.id'))
    lectures=relationship('Lecture', backref='lecture_hall')

class Lecture(Base):
    __tablename__='lectures'
    id=Column(Integer(), primary_key=True)
    unit_name=Column(String(), nullable=False)
    start_time=Column(DateTime())
    lecture_hall_id=Column(Integer(), ForeignKey('lecture_halls.id'))
    lecture_hall=relationship('LectureHall', backref='lectures')
    

engine= create_engine('sqlite:///lecture_hall.db')
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()


def school(name):
    school=School(name=name)
    session.add(school)
    session.commit()
    click.echo(f'{name} added successfully')

def list_schools():
    schools=session.query(School).all()
    print(schools)

def add_lecture_hall(school, name):
    school_obj=session.query(School).filter_by(name=school).first()
    lecture_hall=LectureHall(name=name, school=school_obj)
    session.add(lecture_hall)
    session.commit()






    


