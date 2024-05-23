import numpy as np

a = np.arange(30).reshape(2,15)

print(np.hsplit(a,3) # can splits the array in 3 horizontal sections
)
