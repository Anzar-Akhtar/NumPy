# Slicing = elements ka ek portion/range nikalna

import numpy as np

num = np.array([10, 20, 30, 40, 50, 60])
print(num[1:4])
print(num[:5])
print(num[3:])
print(num[:])
print(num[0:6:2])
print(num[::2])
print(num[::3])

# negative slicing
print(num[-3:])
print(num[-2:])
print(num[::-1])