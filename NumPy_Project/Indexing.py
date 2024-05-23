# Indexing
import numpy as np

"""#Basics

a = np.array([
    [[1,2],
     [3,4]],

    [[5,6],
     [7,8]]
           ]
     )
print(a)

print(a[0,1,1]) # work from outside-in
print(a[:,0,0])

a[:,1,:] = [[9,9],[8,8]]
print(a)
"""

"""
# Boolean Masking and Advanced Indexing

filedata = np.genfromtxt("data.txt", delimiter=",")
print(filedata > 50)  # returns instead of numbers a boolean for the condition
print(filedata[filedata > 50])  # but here grabs the value itself that is true to the condition
print(np.any(filedata > 50, axis=0))  # Axis 0 is columns , it returns true IF 1 is atleast true to the condition
print(np.all(filedata > 50, axis=0))  # here all the column must be True to the condition
print((filedata > 50) & (filedata < 100))  # its prints for every single value a boolean

# You can index with a list
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])  # the insides are indexes not values
"""

#Tips
a = np.array([
    [6, 7, 8],
    [1, 2, 3],
    [9, 3, 2]
])
for cell in a.flat: # flattening it as it a single Dim array , and prints all elements
    print(cell)

b = np.arange(6).reshape(3,2)
c = np.arange(6,12).reshape(3,2)




"""
# SMALL LIL PROJECT

data = np.arange(1,31).reshape(6,5) # instead of below
#data = np.array([
#    [1, 2, 3, 4, 5],
#    [6, 7, 8, 9, 10],
#    [11, 12, 13, 14, 15],
#    [16, 17, 18, 19, 20],
#    [21, 22, 23, 24, 25],
#    [26, 27, 28, 29, 30]
#])

print(data[2:4, 0:2])
print(data[  # indexing with lists
          [0, 1, 2, 3],
          [1, 2, 3, 4]
      ])
print(data[
      [0, -1, -2],
      3:
      ])
"""
