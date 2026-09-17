# axis=0 → rows ke across, yani har column par operation
# axis=1 → columns ke across, yani har row par operation
# axis=0 → column-wise result
# axis=1 → row-wise result


#           Column
#         0    1    2
#       ┌─────────────
# Row 0 │ 10   20   30
# Row 1 │ 40   50   60
# Row 2 │ 70   80   90


import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# sum of column
print(np.sum(data, axis=0))

# sum of row
print(np.sum(data, axis=1))

# mean of column
print(np.mean(data, axis=0))

# mean of row
print(np.mean(data, axis=1))

# max of column
print(np.max(data, axis=0))

# max of column
print(np.max(data, axis=1))

# min of column
print(np.min(data, axis=0))

# min of column
print(np.min(data, axis=1))