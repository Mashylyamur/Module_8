from peewee import *

conn = SqliteDatabase('M8_3.sqlite')

class Students(Model):

    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


class Courses(Model):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')

    class Meta:
        database = conn


class Student_courses(Model):
    student_id = ForeignKeyField(Students, column_name='student_id')
    course_id = ForeignKeyField(Courses, column_name='course_id')

    class Meta:
        database = conn

#Students.create_table()
#Courses.create_table()
#Student_courses.create_table()
#s1 = [{'id':1, 'name':'Max', 'surname':'Brooks', 'age':24, 'city':'Spb'},
#      {'id':2, 'name':'John', 'surname':'Stones', 'age':15, 'city':'Spb'},
#      {'id':3, 'name':'Andy', 'surname':'Wings', 'age':45, 'city':'Manhester'},
#      {'id':4, 'name':'Kate', 'surname':'Brooks', 'age':34, 'city':'Spb'}]
#Students.insert_many(s1).execute()

#c1 = [{'id':1, 'name':'python', 'time_start':'21.07.21', 'time_end':'21.08.21'},
#      {'id':2, 'name':'java', 'time_start':'13.07.21', 'time_end':'16.08.21'}]
#Courses.insert_many(c1).execute()

#sc1 = [{'student_id':1, 'course_id':1},
#       {'student_id':2, 'course_id':1},
#       {'student_id':3, 'course_id':1},
#       {'student_id':4, 'course_id':2}]
#Student_courses.insert_many(sc1).execute()


for student in (Students.select().where(Students.age > 30)):
    print(student.name, student.surname)
print('')
s30 = Students.select().join(Student_courses).join(Courses).where(Courses.id == 1)
for student in s30:
    print(student.name, student.surname)
print('')
s_p = Students.select().join(Student_courses).join(Courses).where(Courses.id == 1, Students.city == 'Spb')
for student in s_p:
    print(student.name, student.surname, student.city)
conn.commit()
conn.close()
