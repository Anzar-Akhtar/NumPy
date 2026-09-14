import numpy as np


# question 1
num = np.array([10, 20, 30, 40, 50])
print(num[0])
print(num[2])
print(num[-1])


# question 2
marks = np.array([78, 85, 92, 67, 88])
print(marks[1])
print(marks[-2])
print(marks[-1])


# question 3
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[0])
print(data[1])
print(data[1, 2])
print(data[2, 1])