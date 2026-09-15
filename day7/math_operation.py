import numpy as np

# addition
add = np.array([10, 20, 30, 40, 50])
print(add + 5)

# substraction
sub = np.array([10, 20, 30, 40, 50])
print(sub - 5)

# multiplication
mul = np.array([10, 20, 30, 40, 50])
print(mul * 2)

# division
div = np.array([10, 20, 30, 40, 50])
print(div / 2)

# power
pow = np.array([10, 20, 30, 40, 50])
print(pow ** 2)

# Adding 2 arrays
a1 = np.array([10, 20, 30])
a2 = np.array([1, 2, 3])
print(a1 + a2)

# Substract 2 arrays
s1 = np.array([10, 20, 30])
s2 = np.array([1, 2, 3])
print(s1 - s2)

# Multiply 2 arrays
m1 = np.array([10, 20, 30])
m2 = np.array([1, 2, 3])
print(m1 * m2)

# Division 2 arrays
d1 = np.array([10, 20, 30])
d2 = np.array([1, 2, 3])
print(d1 / d2)

# Comparison Operation

# greater than
marks = np.array([45, 67, 89, 32, 91])
print(marks > 50)

# less than
marks2 = np.array([45, 67, 89, 32, 91])
print(marks2 < 50)

# greater than or equal
marks3 = np.array([45, 67, 89, 32, 91])
print(marks3 >= 50)

# less than or equal
marks4 = np.array([45, 67, 89, 32, 91])
print(marks4 <= 50)

# equal
marks5 = np.array([45, 67, 89, 32, 91])
print(marks5 == 89)

# mathematical function

# sum
num = np.array([10, 20, 30, 40, 50])
print(np.sum(num))

# minimum
num1 = np.array([10, 20, 30, 40, 50])
print(np.min(num))

# maiximum
num2 = np.array([10, 20, 30, 40, 50])
print(np.max(num))

# mean
marks = np.array([70, 80, 90, 60, 85])
print(np.mean(marks))