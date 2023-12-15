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


