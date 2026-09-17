# Broadcasting = NumPy automatically smaller array/value ko compatible shape ke according adjust karke calculation kar deta hai.

import numpy as np

arr = np.array([10, 20, 30])
# print(arr + 5)


# Scalar ke saath Broadcasting
# print(arr * 2)


# 2D Array + Scalar
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
# print(data + 10)


# Array + Array
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
# print(a + b)


# Broadcasting with Different Shapes
data2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

bonus = np.array([1, 2, 3])
# print(data2 + bonus)


# Feature Adjustment
data3 = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000]
])
adjustment = np.array([1, 2, 5000])
result = data3 + adjustment
# print(result)


# Broadcasting with Column Vector
data4 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
x = np.array([
    [100],
    [200]
])
print(data4 + x)