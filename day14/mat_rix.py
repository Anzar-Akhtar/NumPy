import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
C = A+B
print(C)

# Element wise multiplication
print(A*B)


# for the first row and first column multiplication
print(A@B)


# for the matrix multiplication
res = np.dot(A, B)
print(res)

# matrix determinant
det = np.linalg.det(A)
print(det)


# matrix Inverse
inv = np.linalg.inv(B)
print(inv)