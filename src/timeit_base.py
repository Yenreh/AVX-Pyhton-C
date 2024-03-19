import timeit


def scalar_multiply():
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

    print("Total sum:", total_sum)



# Start measuring time
starting_time = timeit.default_timer()

# Function call
scalar_multiply()

# End measuring time
ending_time = timeit.default_timer()

print(f"Tiempo transcurrido: {ending_time - starting_time}")

