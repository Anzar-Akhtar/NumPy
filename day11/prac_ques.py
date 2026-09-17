import numpy as np

data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000],
    [40, 10, 100000]
])

# question 1:- People whose salary is greater than 50,000
sal = data[:, 2]
print(sal[sal > 50000])

# question 2:- People whose experience is >= 5
exp = data[:, 1]
print(exp[exp >= 5])

# question 3:- People whose age is > 25
age = data[:, 0]
print(age[age > 25])

# question 4:- Indexes of people whose salary is greater than 50,000
print(np.where(sal > 50000))