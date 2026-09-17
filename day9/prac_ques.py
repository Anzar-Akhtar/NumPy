import numpy as np

data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000],
    [40, 10, 100000]
])

# print(np.mean(data, axis=0))

mean = np.mean(data, axis=0)
print(mean)

max = np.max(data, axis=0)
print(max)