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

def display_schools():
    schools = session.query(School).all()
    click.echo(f'Schools: {schools}')

def display_lecture_halls():
    lecture_halls = {hall.id: hall.name for hall in session.query(LectureHall).all()}
    click.echo(f'Lecture Halls: {lecture_halls}')

def display_lectures():
    lectures = {lec.id: lec.unit_name for lec in session.query(Lecture).all()}
    click.echo(f'Lectures: {lectures}')

def update_school():
    school_id = click.prompt('Enter school ID to update', type=int)
    new_name = click.prompt('Enter new school name', type=str)
    school = session.query(School).get(school_id)
    
    if school:
        school.name = new_name
        session.commit()
        click.echo(f'School "{school.name}" updated successfully')
    else:
        click.echo(f'School with ID {school_id} not found.')

