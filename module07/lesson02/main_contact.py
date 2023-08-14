import sys
from sqlalchemy.orm import joinedload
from database.db import session
from database.models import Student, Teacher, ContactPerson, TeacherStudent

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти всіх студентів з вчителями joinedload('teachers')
2 -- Знайти всіх студентів з вчителями .join('teachers')
3 -- Знайти всіх студентів з вчителями joinedload('teachers') по полям
4 -- Знайти всіх студентів з вчителями .join('teachers') полям красиво
"""


def get_students():
    students = session.query(Student).options(joinedload(Student.teachers),
                                              joinedload(Student.contacts, innerjoin=True)).order_by(Student.id).all()
    for s in students:
        column_names = ["id", "fullname", "teachers", "contacts"]
        db = [dict(zip(column_names, (
            s.id, s.fullname, [(t.id, t.first_name) for t in s.teachers], [(c.id, c.first_name) for c in s.contacts])))]
        print(db)


def get_students_join():
    students = session.query(Student).join(Student.teachers).outerjoin(Student.contacts).order_by(Student.id).all()
    for s in students:
        column_names = ["id", "fullname", "teachers", "contacts"]
        db = [dict(zip(column_names, (
            s.id, s.fullname, [(t.id, t.first_name) for t in s.teachers], [(c.id, c.first_name) for c in s.contacts])))]
        print(db)


def custom_get_students():
    students = session.query(Student.id, Student.fullname, Teacher.fullname.label("teacher_fullname"),
                             ContactPerson.fullname.label("contact_fullname")) \
        .select_from(Student).join(TeacherStudent).join(Teacher).join(ContactPerson).all()

    for s in students:
        column_names = ["id", "fullname", "teacher", "contact"]
        db = [dict(zip(column_names, (s.id, s.fullname, s.teacher_fullname, s.contact_fullname)))]
        print(db)


def pretty_custom_get_students():
    # Спочатку отримаємо всіх студентів
    students = session.query(Student).all()

    # Для кожного студента отримаємо його вчителів
    for student in students:
        student.teachers = session.query(Teacher).join(TeacherStudent).filter(
            TeacherStudent.student_id == student.id).all()

    # Також отримаємо контактні особи
    for student in students:
        student.contacts = session.query(ContactPerson).filter(ContactPerson.student_id == student.id).all()

    for s in students:
        column_names = ["id", "fullname", "teachers", "contacts"]
        db = [dict(zip(column_names, (
        s.id, s.fullname, [(t.id, t.first_name) for t in s.teachers], [(c.id, c.first_name) for c in s.contacts])))]
        print(db)


if __name__ == '__main__':
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        match task:
            case 1:
                get_students()
            case 2:
                get_students_join()
            case 3:
                custom_get_students()
            case 4:
                pretty_custom_get_students()
            case _:
                print('Шо це таке?')
