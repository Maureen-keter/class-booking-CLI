import click
from models import School, LectureHall, Lecture, session

def add_school():
    school_name = click.prompt('Enter school name', type=str)
    school = School(name=school_name)
    session.add(school)
    session.commit()
    click.echo(f'School "{school.name}" added successfully')

def add_lecture_hall():
    school_name = click.prompt('Enter school name', type=str)
    school = session.query(School).filter_by(name=school_name).first()

    if not school:
        click.echo(f'School "{school_name}" not found.')
        return

    lecture_hall_name = click.prompt('Enter lecture hall name', type=str)
    lecture_hall = LectureHall(name=lecture_hall_name, school=school)
    session.add(lecture_hall)
    session.commit()
    click.echo(f'Lecture hall "{lecture_hall.name}" added successfully')

def add_lecture():
    lecture_hall_name = click.prompt('Enter lecture hall name', type=str)
    lecture_hall = session.query(LectureHall).filter_by(name=lecture_hall_name).first()

    if not lecture_hall:
        click.echo(f'Lecture hall "{lecture_hall_name}" not found.')
        return

    unit_name = click.prompt('Enter unit name', type=str)
    lecture = Lecture(unit_name=unit_name, lecture_hall=lecture_hall)
    session.add(lecture)
    session.commit()
    click.echo(f'Lecture "{lecture.unit_name}" added successfully')

