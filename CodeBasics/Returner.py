#----------Related to Objects_Classes--------#
class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name

    def display(self):
        print(f'My ID is {self.id} and my name is {self.name}')


#---------------Related to Walkers----------#
class Animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("House")

# No need to write it again as u already extended (Animal)
  #  def print_habitat(self):
  #      print(self.habitat)

    def sound(self):
        print("Woof Woof!")

#----------Related to Inhertiance-------#

class Teacher:
    def teach(self):
        print("Im a Teacher")

class Student(Teacher):
    def study(self):
        print("Im Studying")

class Youtuber(Student):
    def intro(self):
        print("WELCOME BACK TO YOUTUBE!")

""" # Remove the extends () , ex : (Student) in Youtube and (Teacher) in Student to work
class Engineer(Teacher,Student,Youtuber):
    def plan(self):
        print("I can do anything!")
"""

#------Related to CustomException-------#
class AdultException(Exception): # Create your own Exception
    pass # is a null operation or a no-op. It is used when a statement is syntactically required but you don't want to perform any action.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age)>=18:
            raise AdultException # Throws the exception
        else:
            return self.age

    def display_person(self):
        try:
            print(f"age => {self.get_minor_age()}")
        except AdultException:
            print("The Person is an adult You are not allowed to Enter!")
        finally:
            print(f"name ==> {self.name}")
