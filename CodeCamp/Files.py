"""# Reading File

people_file = open("People.txt","r") # "r" = read || "w" = write || "a" append || "r+" = read and write
print(people_file.readable()) #checks if it readable or no
# print(people_file.read())
# print(people_file.readline()) # reads the first line
# print(people_file.readline()) # reads the next line
# print(people_file.readlines()) # reads all of them as a array better than above ↑
# print(people_file.readlines()[1]) # picks an element from the array

for person in people_file.readlines():
    print(person)

people_file.close() # always close a file
"""

""" # Writing Files
"""
people_file = open("people.txt","a") #Adds to already existing file
people_file.write("Toby - Human Resources")
people_file.close()

people_file = open("people1.txt","w") # Override whatever is written || Also can create a new File
people_file.write("Kelly - Customer Service")
people_file.close()
