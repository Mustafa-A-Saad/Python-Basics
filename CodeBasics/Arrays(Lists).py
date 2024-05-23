expenses = [2200,2350,2600,2130,2190]

Q1 = expenses[1] - expenses[-2]
print(Q1)

Q2 = expenses[0]+expenses[1]+expenses[2]
print(Q2)

#Q3
# print("You have spent 2000 Dollars",2000 in expenses)  # Same as below
if 2000 in expenses:
    print("You have spent 2000 Dollars")
else:
    print("False!")

#Q4
# expenses.insert(5,1980) # same as below
expenses.append(1980)
print(expenses)

#Q5
expenses[3] = expenses[3] - 200
print(expenses)

#---------Marvel Heros Project----------#

heros=['Spider man','Thor','Hulk','Iron man','Captain America']

#Q1
print(len(heros))

#Q2
heros.append("Black Panther")
print(heros)

#Q3
heros.remove("Black Panther")
# heros.pop() # same as above
heros.insert(3,"Black Panther")
print(heros)

#Q4
heros[1:3]=["Doctor Strange"]
print(heros)

#Q5
heros.sort()
print(heros)
"""
# Tips
CatNames = ["Tefa","Boogey","Aow"]
name,nickname,exp = CatNames

CatNames.sort(reverse=True) # sorts in reverse ASCIIphetical order , ASCII = Capital letters always comes first [Z,a]
print(CatNames)

CatNames.reverse() # Reverses the lists without any sorting
print(CatNames)

spam = ['A', 'z', 'a', 'Z']
spam.sort(key=str.lower) # Ignores ASCII order and just go aphelitcally
print(spam)
"""

"""
import random
messages = ['It is certain',
 'It is decidedly so',
 'Yes definitely',
 'Reply hazy try again',
 'Ask again later',
 'Concentrate and ask again',
 'My reply is no',
 'Outlook not so good',
 'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
"""


""" #Comma Project
spam = ["apples","bananas","tofu","cats"]

def add(para):
    for i, item in enumerate(para): enumerate() function used to loop over an iterable (like a list) while also keeping track of the index of each item.
        if i == len(para) - 1:
            print(f'and {item}', end="")
        else:
            print(f'{item}, ', end="")

spam = ["apples", "bananas", "tofu", "cats"]
add(spam)
"""

""" # Grid Project

grid = [
 ['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']
]

# Get the number of rows and columns in the grid
num_rows = len(grid) # 9
num_cols = len(grid[0]) # 6

# Iterate over each column of each row to print the image
for y in range(num_cols):
    for x in range(num_rows):
        print(grid[x][y], end="")
    print()  # Print newline after each row

"""

