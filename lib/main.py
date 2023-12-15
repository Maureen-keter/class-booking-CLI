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

def update_lecture_hall():
    hall_id = click.prompt('Enter lecture hall ID to update', type=int)
    new_hall_name = click.prompt('Enter new lecture hall name', type=str)
    lecture_hall = session.query(LectureHall).get(hall_id)

    if lecture_hall:
        lecture_hall.name = new_hall_name
        session.commit()
        click.echo(f'Lecture hall "{lecture_hall.name}" updated successfully')
    else:
        click.echo(f'Lecture hall with ID {hall_id} not found.')

def delete_school():
    delete_school_name = click.prompt('Enter school name to delete', type=str)
    school_to_delete = session.query(School).filter_by(name=delete_school_name).first()

    if school_to_delete:
        session.delete(school_to_delete)
        session.commit()
        click.echo(f'School "{delete_school_name}" deleted successfully')
    else:
        click.echo(f'School "{delete_school_name}" not found.')

def delete_lecture_hall():
    delete_hall_name = click.prompt('Enter lecture hall name to delete', type=str)
    hall_to_delete = session.query(LectureHall).filter_by(name=delete_hall_name).first()

    if hall_to_delete:
        session.delete(hall_to_delete)
        session.commit()
        click.echo(f'Lecture hall "{delete_hall_name}" deleted successfully')
    else:
        click.echo(f'Lecture hall "{delete_hall_name}" not found.')

if __name__ == '__main__':
    function_to_run = click.prompt(
        'Choose a function to run:\n'
        '1. add_school\n'
        '2. add_lecture_hall\n'
        '3. add_lecture\n'
        '4. display_schools\n'
        '5. display_lecture_halls\n'
        '6. display_lectures\n'
        '7. update_school\n'
        '8. update_lecture_hall\n'
        '9. delete_school\n'
        '10. delete_lecture_hall\n',
        type=int
    )

    if function_to_run == 1:
        add_school()
    elif function_to_run == 2:
        add_lecture_hall()
    elif function_to_run == 3:
        add_lecture()
    elif function_to_run == 4:
        display_schools()
    elif function_to_run == 5:
        display_lecture_halls()
    elif function_to_run == 6:
        display_lectures()
    elif function_to_run == 7:
        update_school()
    elif function_to_run == 8:
        update_lecture_hall()
    elif function_to_run == 9:
        delete_school()
    elif function_to_run == 10:
        delete_lecture_hall()
    else:
        click.echo('Invalid option. Please choose a valid function.')






