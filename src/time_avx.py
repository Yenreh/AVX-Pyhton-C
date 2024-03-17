import ctypes

# Definition of constants
n = 10000000
lst = range(0, n)
x = 2

fun = ctypes.CDLL('./lib_AVX.so')

