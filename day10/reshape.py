# reshape() — Array ka shape change karna

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.shape)

arr2 = arr.reshape(2, 3)
print(arr2)


# -1 in reshape is shortcut NumPy khud calculate karega ki second dimension kya honi chahiye.
print(arr.reshape(2, -1))