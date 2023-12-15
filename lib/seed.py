from faker import Faker
from sqlalchemy.orm import Session
from models import School, LectureHall, Lecture, engine, Base

fake = Faker()

def generate_fake_schools(session, num_schools=5):
    for _ in range(num_schools):
        school_name = fake.company()
        school = School(name=school_name)
        session.add(school)
    session.commit()

def generate_fake_lecture_halls(session, num_lecture_halls=10):
    schools = session.query(School).all()

    for _ in range(num_lecture_halls):
        lecture_hall_name = fake.unique.word()
        school = fake.random_element(schools)
        lecture_hall = LectureHall(name=lecture_hall_name, school=school)
        session.add(lecture_hall)
    session.commit()

