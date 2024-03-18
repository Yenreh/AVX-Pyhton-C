import numpy as np
import timeit


n = 10000000
lst = range(n)
x = 2
v1 = np.array(lst)
v2 = np.array(lst)





for i in range(n):
    v2[i] = 1

total_sum = 0
for i in range(n):
    total_sum += (v1[i] + 1) * v2[i]

print("Total sum:", total_sum)

