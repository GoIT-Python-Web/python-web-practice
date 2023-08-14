import sys

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database.db import session
from database.models import Student, Teacher, ContactPerson, TeacherStudent


def get_students():
    stmt = select(Student).join(Student.teachers).outerjoin(Student.contacts).order_by(Student.id)

    students = session.execute(stmt).scalars().all()
    for s in students:
        column_names = ["id", "fullname", "teachers", "contacts"]
        db = [dict(zip(column_names, (
            s.id, s.fullname, [(t.id, t.first_name) for t in s.teachers], [(c.id, c.first_name) for c in s.contacts])))]
        print(db)


if __name__ == '__main__':
    get_students()
