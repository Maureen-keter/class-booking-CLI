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

def generate_fake_lectures(session, num_lectures=20):
    lecture_halls = session.query(LectureHall).all()

    for _ in range(num_lectures):
        unit_name = fake.catch_phrase()
        start_time = fake.date_time_this_decade()
        end_time = start_time + fake.time_delta()

        lecture_hall = fake.random_element(lecture_halls)
        lecture = Lecture(unit_name=unit_name, start_time=start_time, end_time=end_time, lecture_hall=lecture_hall)
        session.add(lecture)
    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    generate_fake_schools(session)
    generate_fake_lecture_halls(session)
    generate_fake_lectures(session)

