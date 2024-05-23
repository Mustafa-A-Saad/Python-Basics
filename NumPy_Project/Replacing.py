# Replacing
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14]]
             )  # 2 by 7 array
print(a.shape)  # prints rows and cols , here is 2 row 7 col

print(a[1, 5])  # a[row,col] gets a specific
print(a[1, -2])  # there is also -ve like normal

print(a[0, :])  # get a of a specfic row
print(a[:, 1])  # get a specific col

print(a[0, 1:6:2])  # [startIndex:endIndex:stepsize]

a[1, 5] = 20  # replacing
print(a)

a[:, 2] = 5  # replaced all of col 2 to 5
print(a)

a[:, 2] = [1, 2]  # replace but 2 diff numbers
