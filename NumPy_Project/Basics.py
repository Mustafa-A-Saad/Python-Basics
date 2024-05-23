# Basics
# NumPy is so much faster than lists in normal python and have much more flexibility in handling arrays
import sys
import time
import numpy as np

a = np.array([1,2,3] ,dtype='int16') #
print(a)

# you can nest how much lists as you want
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

print(a.ndim) # number of dim
print(b.ndim)

print(a.shape) # how many rows and cols
print(b.shape)

print(a.dtype) # types in memory ( defualt in32 ) but i changed it to int16 for less mem
print(b.dtype)

print(a.itemsize)  # get size of all elements in byte
print(b.itemsize)

print(a.nbytes) # total size = a.size * a.itemsize
print(b.nbytes)

#---------------------Lists in python vs Array Numpy-------------------#

# sys.getsizeof(5) returns the size of the integer 5 in bytes. # can be any int
# Multiplying it by the length of the nor_list gives the total size of the list in bytes.
nor_list = range(1000) # creates a list from 0-999
print(sys.getsizeof(5)*len(nor_list))

# np_array.size returns the number of elements in the array, and np_array.itemsize returns the size of each element in bytes.
np_array = np.arange(1000)
print(np_array.size*np_array.itemsize)

#np array takes WAY less memory

"""
import sys
import time
import numpy as np

size = 1000000

list1 = range(size)
list2 = range(size)

arr1 = np.arange(size)
arr2 = np.arange(size)

#Python list
start = time.time()
result = [(x+y) for x,y in zip(list1,list2)] # list comprehension
print("python list took: ",(time.time()-start)*1000)

#Numpy List

start = time.time()
result = arr1 + arr2
print("numpy took: ",(time.time()-start)*1000) # Calculates the time taken for the operation by subtracting the start time from the current time
# As you see numpy gets done in way less time
"""





