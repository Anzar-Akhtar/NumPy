# ndim:- number of dimensions

import numpy as np

a = np.array([10, 20, 30, 40])
print(a.ndim)

b = np.array([
    [10, 20],
    [30, 40]
])
print(b.ndim)

c = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])
print(c.ndim)