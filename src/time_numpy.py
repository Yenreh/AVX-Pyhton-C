import numpy as np
import timeit

# Definition of constants
n = 10000000
lst = range(0, n)
x = 2


def scalar_multiplication():
    # Vector creation using numpy
    v = np.array(lst)
    # Scalar multiplication
    for i in lst:
        v[i] = v[i] * x


# Start measuring time
starting_time = timeit.default_timer()

# Function call
scalar_multiplication()

# End measuring time
ending_time = timeit.default_timer()

print(f"Tiempo transcurrido: {ending_time - starting_time}")

