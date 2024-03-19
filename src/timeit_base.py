import numpy as np
import timeit


def scalar_multiply():
    # Definition of constants
    n = 10000000
    lst = range(0, n)
    x = 2

    # Vector creation using numpy
    v = np.array(lst)

    # Scalar multiplication
    for i in lst:
        v[i] = v[i] * x


# Start measuring time
starting_time = timeit.default_timer()

# Function call
scalar_multiply()

# End measuring time
ending_time = timeit.default_timer()

print(f"Tiempo transcurrido: {ending_time - starting_time}")

