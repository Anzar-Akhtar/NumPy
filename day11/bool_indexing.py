import numpy as np

marks = np.array([45, 67, 89, 32, 91, 76])
print(marks > 70)
print(marks[marks > 70])
print(marks[marks < 70])
print(marks[marks >= 70])
print(marks[marks <= 70])
print(marks[marks == 70])
print(marks[(marks > 60) & (marks < 90)])
print(marks[(marks < 50) | (marks > 90)])



data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000],
    [40, 10, 100000]
])

salary = data[:, 2]
print(salary[salary > 50000])


# Agar hume poori row chahiye jahan salary > 50000
print(data[data[:, 2] > 50000])