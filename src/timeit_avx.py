import ctypes
import timeit

# Load the shared library into ctypes
lib_avx = ctypes.CDLL('./lib_AVX.so')


def scalar_multiply():
    # Define the function prototype to be able to call it with python data types
    vectorScalarMultiply = lib_avx.vectorScalarMultiply
    vectorScalarMultiply.argtypes = [
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_double,
        ctypes.POINTER(ctypes.c_double),
        ctypes.c_int
    ]

    # Definition of constants and casting to ctypes
    n = 10000000
    vector = (ctypes.c_double * n)(*range(n))
    scalar = ctypes.c_double(2)
    result = (ctypes.c_double * n)()

    # Call the function
    vectorScalarMultiply(vector, scalar, result, ctypes.c_int(n))


# Start measuring time
starting_time = timeit.default_timer()

scalar_multiply()

# End measuring time
ending_time = timeit.default_timer()

print(f"Tiempo transcurrido: {ending_time - starting_time}")