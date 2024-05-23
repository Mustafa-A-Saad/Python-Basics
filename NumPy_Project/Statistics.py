import numpy as np

stats = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(stats)
print(np.min(stats))  # min of the whole list
print(np.min(stats, axis=0))  # Print the minimum value along axis 0 (columns)
print(np.min(stats, axis=1))  # Print the minimum value along axis 1 (rows)
print(np.max(stats))

print(np.sum(stats))  # sums everything
print(np.sum(stats, axis=0))  # sums value along axis 0 ( cols )
print(np.sum(stats, axis=1))  # sums value along axis 1 ( rows )
