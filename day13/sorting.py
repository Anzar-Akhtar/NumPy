# Sorting ka matlab values ko order mein arrange karna.

import numpy as np
arr = np.array([50, 20, 80, 10, 40])
res = np.sort(arr)
print(res)


# descending order
res2 = np.sort(arr)[::-1]
print(res2)