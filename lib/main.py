import click
from sqlalchemy.orm import joinedload
from models import School, LectureHall, Lecture, session

def add_school(school_name):
    school = School(name=school_name)
    session.add(school)
    session.commit()
    click.echo(f'{school_name} added successfully')

def list_schools():
    schools = session.query(School).all()
    print(schools)
    return schools

def add_lecture_hall(school_name, lecture_hall_name):
    school = session.query(School).filter_by(name=school_name).first()
    if not school:
        click.echo(f'{school_name} does not exist.')
        return
    lecture_hall = LectureHall(name=lecture_hall_name, school=school)
    session.add(lecture_hall)
    session.commit()
    click.echo(f'{lecture_hall} added successfully')

def add_lecture(lecture_hall_name, unit_name):
    lecture_hall = session.query(LectureHall).options(joinedload('lectures')).filter_by(name=lecture_hall_name).first()

    if not lecture_hall:
        click.echo(f'Lecture hall "{lecture_hall_name}" does not exist.')
        return
    lecture = Lecture(unit_name=unit_name, lecture_hall=lecture_hall)
    session.add(lecture)
    session.commit()
    click.echo(f'Lecture "{unit_name}" added to lecture hall "{lecture_hall_name}".')


