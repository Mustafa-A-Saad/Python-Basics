""" # Methods Basics

def method(): # must be indented
    print("Hello User")
    user = input("Enter your Name")
    print("Welcome " + user)

def method2(name,age):
    print("Hello " + name + " you are " + str(age))

method()

method2("Tefa",20)

"""

""" # Returns Methods

def cube(x):
   return pow(x,3)

print(cube(3))

def getsum(x,y):
    return x+y

print(getsum(3,5))
"""


""" # Expo Function

print(2**3) # 2 power of 3 = pow 2,3
print(pow(2,3))

def expo(base,power):
    result = 1
    for index in range(power): # starts from 0 to power-1 
        result = result * base
    return result

print(expo(2,5))

"""

