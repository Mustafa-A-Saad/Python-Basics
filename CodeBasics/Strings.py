street = "Sarai"
city = "Alexandria"
country = "Egypt"
adresss = street+ " " + city + " " + country
print(adresss)

# using Printf

adresss = f'{street}\n{city}\n{country}'
print(adresss)

num_fruits= input("Number of fruits u eat ")
num_veggies=input("Number of Veggies u eat ")
sentence = f"I eat {num_veggies} veggies and {num_fruits} daily"
print(sentence)

# Slice Operator

phrase='Earth revolves around the sun'
print(phrase[6:14])
print(phrase[-3:])

# Replacing

s = 'maine 200 banana khaye'
s = s.replace("200","10",).replace("banana","samosa")
print(s)

# File without Extensions
file_name = input("Enter a file name with extension")
print(file_name[0:len(file_name)-4])
"""
# Tips
'hello'.isalpha() # consists only of letters
'hello123'.isalpha() #
'hello123'.isalnum() # consists only of letters and numbers
'hello'.isalnum() # 
'123'.isdecimal() # consists only of numeric characters
' '.isspace() # consists only of spaces, tabs,
'This Is Title Case'.istitle() # consists only of words that begin with n uppercase letter followed by only lowercase letters.


while True:
 print('Enter your age:')
 age = input()
 if age.isdecimal():
 break
 print('Please enter a number for your age.')
while True:
 print('Select a new password (letters and numbers only):')
 password = input()
 if password.isalnum():
 break
 print('Passwords can only have letters and numbers.')


print(' Tefa '.join(['My', 'name', 'is', 'Simon']))

print('My name is Simon'.split()) # puts every word in a list

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))


print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-')) # left justify
print('Hello'.center(20, '='))
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth,) + ":" + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
