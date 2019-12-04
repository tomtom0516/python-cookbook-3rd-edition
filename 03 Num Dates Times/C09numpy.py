import numpy as np

grid = np.zeros(shape=(10000,10000), dtype=float)
grid += 10

# row and column
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# select column 1
a[:,1]

# select subregion
a[0:3, 0]

# 