# dtype:- btata hai ke elements ka data type kya hai

import numpy as np
a = np.array([1, 2, 3])
print(a.dtype)

b = np.array([1.2, 2.3, 3.4])
print(b.dtype)

# manually

c = np.array([2, 3, 4], dtype=float)
print(c)
print(c.dtype)