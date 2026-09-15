import numpy as np

# question1:- basic slicing
num = np.array([10, 20, 30, 40, 50, 60, 70])
# print(num[1:4])

# question2:- Reverse an array
# print(num[::-1])

# question3:- 2D slicing
data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# first and last 2 rows
print(data[:2])
print(data[-2:])

# first and last 2 column
print(data[:, :2])
print(data[:, -2:])


# question4:- AI/ML dataset
data1 = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000]
])
print(data1[:, 0]) # all ages
print(data1[:, 1]) # all experience value
print(data1[:, 2]) # all salaries
print(data1[:, 0:2]) # age + experience 
print("\n")



# question5:- ML challenge
data2 = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000],
    [35, 7, 80000]
])

x = data2[:, 0:2]
print(x)

y = data2[:, 2]
print(y)