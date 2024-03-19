
import cProfile as profile
import pstats


prof = profile.Profile()


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



# Start profiling
prof.enable()

# Function call
scalar_multiply()

# End profiling
prof.disable()

stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
stats.print_stats(10)
