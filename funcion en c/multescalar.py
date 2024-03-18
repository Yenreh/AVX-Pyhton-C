import timeit
import ctypes
starting_time = timeit.default_timer()

fun = ctypes.CDLL("/home/ervin/Escritorio/vectorScalarMultiply  /funcion en c/multescalar-AVX.so")

ending_time = timeit.default_timer()
print(f"Tiempo transcurrido {ending_time - starting_time}")
