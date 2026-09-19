import numpy as np

# ques1:- generate the 5 random interger numbers between 1 to 100
ran_int = np.random.randint(1, 51, 5)
print(ran_int)


# ques2:- Random Dataset
data = np.random.randint(1, 101,10)
print(data)

max = np.max(data)
print(max)

min = np.min(data)
print(min)

avg = np.mean(data)
print(avg)


# ques3:- matrix operations
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
print(A + B)

print(A - B)

print(A * B)

print(A @ B)



# ques4:- matrix transpose
A1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
shape = np.shape(A1)
print(shape)

trans = np.transpose(A1)
print(trans)

trans_shape = np.shape(trans)
print(trans_shape)



# ques5:- AI/ML practice
data = np.array([
    [20, 1, 25000],
    [25, 3, 40000],
    [30, 5, 60000]
])

# find the shape
data_shape = np.shape(data)
print(data_shape)

# find the mean of the every column of the dataset
mean = np.mean(data, axis=0)
print(mean)

# find the transpose of the dataset
data_trans = np.transpose(data)
print(data_trans)


# random 3X3 matrix
rand_mat = np.random.randint(1, 100, (3, 3))
print(rand_mat)

# find the determinant of the random 3X3 matrix
rand_mat_det = np.linalg.det(rand_mat)
print(rand_mat_det)