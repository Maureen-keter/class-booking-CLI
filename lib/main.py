import click
from models import School, LectureHall, Lecture, session


school_name = click.prompt('Enter school name', type=str)
school = School(name=school_name)
session.add(school)
session.commit()
click.echo(f'School "{school.name}" added successfully')


school = session.query(School).filter_by(name=school_name).first()
lecture_hall_name = click.prompt('Enter lecture hall name', type=str)
lecture_hall = LectureHall(name=lecture_hall_name, school=school)
session.add(lecture_hall)
session.commit()
click.echo(f'Lecture hall "{lecture_hall.name}" added successfully')


lecture_hall = session.query(LectureHall).filter_by(name=lecture_hall_name).first()
unit_name = click.prompt('Enter unit name', type=str)
lecture = Lecture(unit_name=unit_name, lecture_hall=lecture_hall)
session.add(lecture)
session.commit()
click.echo(f'Lecture "{lecture.unit_name}" added successfully')


schools = session.query(School).all()
click.echo(f'Schools: {schools}')


lecture_halls = {hall.id: hall.name for hall in session.query(LectureHall).all()}
click.echo(f'Lecture Halls: {lecture_halls}')


lectures = {lec.id: lec.unit_name for lec in session.query(Lecture).all()}
click.echo(f'Lectures: {lectures}')


school_id = click.prompt('Enter school ID to update', type=int)
new_name = click.prompt('Enter new school name', type=str)
school = session.query(School).get(school_id)
if school:
    school.name = new_name
    session.commit()
    click.echo(f'School "{school.name}" updated successfully')
else:
    click.echo(f'School with ID {school_id} not found.')


hall_id = click.prompt('Enter lecture hall ID to update', type=int)
new_hall_name = click.prompt('Enter new lecture hall name', type=str)
lecture_hall = session.query(LectureHall).get(hall_id)
if lecture_hall:
    lecture_hall.name = new_hall_name
    session.commit()
    click.echo(f'Lecture hall "{lecture_hall.name}" updated successfully')
else:
    click.echo(f'Lecture hall with ID {hall_id} not found.')


delete_school_name = click.prompt('Enter school name to delete', type=str)
school_to_delete = session.query(School).filter_by(name=delete_school_name).first()
if school_to_delete:
    session.delete(school_to_delete)
    session.commit()
    click.echo(f'School "{delete_school_name}" deleted successfully')
else:
    click.echo(f'School "{delete_school_name}" not found.')


delete_hall_name = click.prompt('Enter lecture hall name to delete', type=str)
hall_to_delete = session.query(LectureHall).filter_by(name=delete_hall_name).first()
if hall_to_delete:
    session.delete(hall_to_delete)
    session.commit()
    click.echo(f'Lecture hall "{delete_hall_name}" deleted successfully')
else:
    click.echo(f'Lecture hall "{delete_hall_name}" not found.')




