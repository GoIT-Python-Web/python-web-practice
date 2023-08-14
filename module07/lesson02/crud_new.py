from sqlalchemy import select, update, delete

from database.db import session
from database.models import Student, Teacher
from faker import Faker
fake = Faker()


def add_student(teacher_ids: list):
    stmt = select(Teacher).where(Teacher.id.in_(teacher_ids))

    teachers = session.execute(stmt).scalars().all()
    student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            teachers=teachers
        )
    session.add(student)
    session.commit()
    return student


def update_student(student_id: int, teacher_ids: list):
    stmt = select(Teacher).where(Teacher.id.in_(teacher_ids))
    teachers = session.execute(stmt).scalars().all()
    print(teachers)
    stmt = select(Student).filter_by(id=student_id)
    student = session.execute(stmt).scalar_one()
    print(student)
    student.teachers = teachers
    session.commit()

    return student


def remove_student(student_id: int):
    stmt = select(Student).filter_by(id=student_id)
    student = session.execute(stmt).scalar_one()
    print(student.id, student.first_name)
    session.delete(student)
    session.commit()
    student = session.query(Student).filter(Student.id == student_id).first()
    print(student)


if __name__ == '__main__':
    st = add_student([1, 2])
    print('---- Add student -----')
    print(st.id, st.first_name)
    for t in st.teachers:
        print(t.id, t.first_name)

    st = update_student(st.id, [3, 4])
    print('---- Update student -----')
    print(st.id, st.first_name)
    for t in st.teachers:
        print(t.id, t.first_name)

    print('---- Remove student -----')
    remove_student(st.id)
