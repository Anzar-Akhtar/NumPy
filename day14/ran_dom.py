# np.random:- NumPy mein random numbers generate karne ke liye:

import numpy as np


# np.random.rand():- Random numbers generate karta hai jo generally 0 se 1 ke beech hote hain.
num = np.random.rand(5)
print(num)


# 2D
num_2D = np.random.rand(2, 3)
print(num_2D)


# np.random.randint():- if we want an integer numbers
num_int = np.random.randint(1, 10, 5)
print(num_int)


# 2D
num_int_2D = np.random.randint(10, 100, (3, 4))
print(num_int_2D)



# np.random.choice:- Iska use kisi given collection mein se random values choose karne ke liye hota hai.

names = np.array(["A", "B", "C", "D", "E"])
result = np.random.choice(names, 2)
print(result)


# np.random.seed():- Agar hum same random result reproduce karna chahte hain
np.random.seed(42)
print(np.random.rand(3))