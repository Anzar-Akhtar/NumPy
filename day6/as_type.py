# astype():- ka use existing NumPy array ka data type convert karne ke liye hota hai.

import numpy as np

# int -> float
arr = np.array([10, 20, 30])
float_arr = arr.astype(float)
print(float_arr)


# float -> int
arr2 = np.array([1.1, 2.2, 3.3])
int_arr = arr2.astype(int)
print(int_arr)


# int -> string
arr3 = np.array([1, 2, 3, 4, 5])
str_arr = arr3.astype(str)
print(str_arr)