from sqlalchemy import and_, or_
from sqlalchemy.orm import Session as SQLSession

from modules.database import Session
from modules.lesson import Lesson, association_table
from modules.students import Student
from modules.group import Group


session: SQLSession = Session()
print(f'Кол-во студентов: {session.query(Student).count()}')

student = session.query(Student).filter(and_(Student.surname.like('Д%'), Student.age > 18)).one()
print(student)
print('*'*30)

students = session.query(Student).filter(and_(Student.surname.like('А%'), Student.age > 16))
for it in students:
    print(it)
print('*' * 30)

students_list: list[Student] = [it for it in students]
print(students_list)
print('*'*30)
for it in session.query(Student).filter(or_(Student.surname.like('Д%'), Student.surname.like('В%'))):
    print(it)
print('*' * 30)

student_query = session.query(Student).join(Group).filter(Group.group_name == '1-МДА-9')
for it in student_query:
    print(it)
print(f'Кол-во студентов: {student_query.count()}')
print('*' * 30)

for it in session.query(Lesson):
    print(it)
print('*' * 30)

for it in session.query(Lesson).filter(Lesson.id > 3):
    print(it)
print('*' * 30)

for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
    print(it)
print('*' * 30)

for it, _ in session.query(Lesson.lesson_title, Group.group_name).filter(and_(
    association_table.c.lesson_id == Lesson.id,
    association_table.c.group_id == Group.id,
    Group.group_name == '1-МДА-7')):
    print(it)
print('*' * 30)
print(session.query(Student).get(40))
print(session.query(Student).get(60))

session.close()