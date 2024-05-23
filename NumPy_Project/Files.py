import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]] , dtype='int32')
np.savetxt("test.txt",x) # creates / saves a file

# Loading the data from the text file "test.txt" into a new NumPy array 'y'.
y = np.loadtxt("test.txt") # displays the text
print(y)
