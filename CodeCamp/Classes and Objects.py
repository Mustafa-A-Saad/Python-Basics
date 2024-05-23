# Classes = Defining your own Data type ( a Student )
# Student.py is related
# Object = an acutal instance of the class (an acutal student ) OOP

from Student import Student

student1 = Student("Jim","20","CS","3.5",True)
student1 = Student("Boogey","17","Data Engineer","3.1",False)

print(student1.name)
print(student1.major)
print(student1.is_smart)