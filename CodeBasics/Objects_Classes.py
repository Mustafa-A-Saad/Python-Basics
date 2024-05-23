from Returner import Employee

# Creating a emp instance of Employee class
employee1 = Employee("Jimmy","23012069")
employee2 = Employee("Ricky","23069102")

print(employee1.id)
employee1.display()

del employee1.id
del employee1

try:
    print(employee1.id)
except NameError:
    print("Emp id is removed")

try:
    employee1.display()
except NameError:
    print("Emp is not defined")
