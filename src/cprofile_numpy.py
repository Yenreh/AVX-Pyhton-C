import numpy as np
import cProfile as profile
import pstats

prof = profile.Profile()

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


# Start profiling
prof.enable()

# Function call
scalar_multiplication()

# End profiling
prof.disable()

stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
