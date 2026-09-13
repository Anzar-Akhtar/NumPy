import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70]
])

print("Array:")
print(marks)

print("Shape:", marks.shape)
print("Size:", marks.size)
print("Dimension:", marks.ndim)
print("Data type:", marks.dtype)
print("Item size:", marks.itemsize)
print("Total size:", marks.nbytes)