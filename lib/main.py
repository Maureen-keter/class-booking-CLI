import click
from models import School, LectureHall, Lecture, session

def add_school():
    school_name = click.prompt('Enter school name', type=str)
    school = School(name=school_name)
    session.add(school)
    session.commit()
    click.echo(f'School "{school.name}" added successfully')

