# splitting:- ek bade array ko chote array mai convert karna

import numpy as np


# np.split()
# ise jab hi use karte hai jab arr equally divide ho sakta ho
arr = np.array([10, 20, 30, 40, 50, 60])
res = np.split(arr, 3)
print(res)


# np.array_split()
res1 = np.array_split(arr, 2)
print(res)