# Agar array mein duplicate values hain aur humein sirf unique values chahiye:

import numpy as np
arr = np.array([10, 20, 20, 40, 60, 60, 70, 80, 80])
res = np.unique(arr)
print(res)