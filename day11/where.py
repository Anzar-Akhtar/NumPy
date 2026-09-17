# np.where():- Hume find karna hai ki 80 se zyada marks kis index par hain.


import numpy as np
marks = np.array([45, 67, 89, 32, 91, 76])
print(np.where(marks > 80))


# Agar actual values chahiye:
indices = np.where(marks > 80)[0]
print(indices)
print(marks[indices])

# np.where(condition, value_if_true, value_if_false)

result = np.where(marks >= 50, "Pass", "Fail")
print(result)