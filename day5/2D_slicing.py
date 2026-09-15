import numpy as np

data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [25, 7, 80000]
])

print(data[:2]) # means 2 rows
print(data[-2:]) #means last 2 rows

# array[row_start:row_stop, column_start:column_stop]
print(data[0:2, 0:2])

print(data[:, 0]) # : all rows, 0 means column 0
print(data[:, 2])

print(data[:, 0:2]) # all rows, column 0 and 1
print(data[0:2, 0:2])