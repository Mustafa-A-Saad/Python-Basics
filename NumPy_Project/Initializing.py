import numpy as np

print(np.zeros(5))  # All 0 vector
print(np.zeros((2, 3)))  # You can do any dim

print(np.ones((4, 2, 2), dtype='int32'))  # 1 matrix

print(np.full((2, 2), 99, dtype='float32'))  # any other number

print(np.random.rand(4, 2))  # just random matrix floats

print(np.random.randint(-2, 7, size=(3, 3)))  # just random matrix integers

print(np.identity(3))  # identity matrix

arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3)  # repeats the array in 1 list
# to use axis list must be 2D+
r2 = np.repeat(arr, 3, axis=0)  # create 3 identical lists
r3 = np.repeat(arr, 3, axis=1)  # the defualt like r1
print(f"no axis {r1}")
print(f"axis 0 {r2}")
print(f"axis 1 {r3}")

print(np.linspace(1, 5, 20))  # it will do a list that is linearly spaced

a = np.array([[1, 2], [3, 4], [5, 6]]) # shape = 3 ,2
a = a.reshape(2,3) # reshpaes it
print(a)
a = a.ravel() # here ravel makes it 1 dim in ( 1 row )
print(a)






""" # lil project
import numpy as np

a = np.ones((5,5))
a[1:4,1:4] = 0
a[2,2] = 9
print(a)

# 2 ways to do it

b= np.ones((5,5))
z =np.zeros((3,3))
z[1,1] = 9
b[1:-1,1:-1]=z
print(b)
"""
