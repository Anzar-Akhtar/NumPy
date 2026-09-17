# transpose() converted rows into column

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

trans = data.transpose()
print(trans)

# shortcut:- data.T
print(data.T)