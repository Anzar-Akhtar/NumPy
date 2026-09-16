import numpy as np

data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000],
    [40, 10, 100000]
])

# average age
age = data[:, 0]
avg_age = np.mean(age)
print(avg_age)


# maximum experience
exp = data[:, 1]
max_exp = np.max(exp)
print(max_exp)


# minimum salary
sal = data[:, 2]
min_sal = np.min(sal)
print(min_sal)


# maximum salary
max_sal = np.max(sal)
print(max_sal)


# maximum salary index
max_sal_ind = np.argmax(sal)
print(max_sal_ind)


# complete row for maximum salary person
print(data[max_sal_ind])