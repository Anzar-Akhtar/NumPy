import numpy as np

data = np.array([
    [20,1,25000],
    [25,3,40000],
    [30,5,60000],
    [35,7,80000],
    [40,10,100000]
])

# question 1:- find original shape
ori_shape = np.shape(data)
print(ori_shape)

# question 2:- Reshape it into(3, 5)
re_shape = data.reshape(3, 5)
print(re_shape)

# question 3:- flatten the dataset
flat = data.flatten()
print(flat)

# Transpose the dataset
trans = data.transpose()
print(trans)

# Shape after transpose
print(np.shape(trans))