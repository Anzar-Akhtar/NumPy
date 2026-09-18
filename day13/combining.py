# Combining ka matlab hai 2 ya more arrays ko ek saath join karna.

import numpy as np

# concatenate:- means kisi do arrays ko jodna
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

res = np.concatenate((a, b))
print(res)



a1 = np.array([
    [1, 2],
    [3, 4]
])

b1 = np.array([
    [5, 6],
    [7, 8]
])

res1 = np.concatenate((a1, b1), axis=0) #axis=0 means row add krni hai
print(res1)
res2 = np.concatenate((a1, b1), axis=1) #axis=1 means column add honge
print(res2)


# vstack = vertical stack:- Yaani arrays ko upar-niche jodna.
res3 = np.vstack((a,b))
print(res3)


# hstack = horizontal stack:- Yaani arrays ko side-by-side jodna.

res4 = np.hstack((a, b))
print(res4)