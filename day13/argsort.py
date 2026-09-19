# argsort() values nahi, indexes return karta hai.

import numpy as np

marks = np.array([80, 70, 75, 98])
index = np.argsort(marks)
print(index)