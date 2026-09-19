import numpy as np

data1 = np.array([
    [20, 1, 25000],
    [25, 3, 40000]
])

data2 = np.array([
    [30, 5, 60000],
    [35, 7, 80000]
])


# combine both data
com = np.concatenate((data1, data2))
print(com)

# sort the salary column
sal = com[:, 2]
sal_sort = np.sort(sal)
print(sal_sort)

# find the unique salaries
uni_sal = np.unique(sal)
print(uni_sal)

# print the shape of the data
shape = np.shape(com)
print(shape)