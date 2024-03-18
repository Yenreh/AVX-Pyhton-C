import timeit

starting_time1 = timeit.default_timer()
n = 10000000
lst = list(range(n))
x = 2
v1 = lst[:]
v2 = lst[:]

for i in range(n):
    v2[i] = 1

total_sum = 0
for i in range(n):
    total_sum += (v1[i] + 1) * v2[i]
ending_time1 = timeit.default_timer()

print(ending_time1 - starting_time1)


