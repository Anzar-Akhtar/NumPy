# ravel() also convert 2D into 1D

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

flat = data.ravel()
print(flat)