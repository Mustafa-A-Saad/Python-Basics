""" #Basics
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are not male or tall")

"""

"""

def Largest(x,y,z):
    biggest =  max(max(x,y),z)
    return biggest

print(Largest(3,2,5))
"""

""" # While loop

i = 1
while i<=10:
    print(i)
    i += 1
"""

""" # For Loops
friends = ["Bob","Rick","Morty"]

for letter in "BoogeyMan":
    print(letter)

for friend in friends:
    print(friend)

for index in range(10):# not including 10
    print(index)

for index2 in range(3,10): # from 3 to 10
    print(index2)

for array in range(len(friends)):
    print(friends[array])

for project in range(5): # starts from 0 
    if project==0:
        print("First Iteration")
    else:
        print("Not First")
"""



