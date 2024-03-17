#!/bin/bash

#remove in src folder the file lib_AVX.so
rm -f src/lib_AVX.so

#compile the file avx.c in src folder
#gcc -fPIC -shared -o lib_AVX.so src/avx.c

#compile the file avx.c in src folder with the flag -mavx to use the AVX instructions
gcc -fPIC -shared -o src/lib_AVX.so -mavx src/avx.c
