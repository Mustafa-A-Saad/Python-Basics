import numpy as np

before = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(before)

after = before.reshape((8, 1))  # reshapes an array dim
print(after)

# Vertical Stacking
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])  # vectors must be same number of elements otherwise mismatch
print(np.vstack([v1, v2]))  # Vertically Stacking vectors or matrices , puts them in a list together
print(np.vstack([v1, v2, v2, v1]))  # You can duplicate as you like

# Horizontal Stacking
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))
print(h1)
print(h2)
print(np.hstack([h1, h2]))  # Stacking horizontal

a = np.arange(30).reshape(2, 15)

print(np.hsplit(a, 3)  # can split the array in 3 horizontal sections
      )
