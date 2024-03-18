#!/bin/bash

# Definir el número de iteraciones
num_iteraciones=5
resultados=()

# Iterar sobre el script de Python y almacenar los resultados
for ((i=0; i<num_iteraciones; i++)); do
    tiempo=$(python3 multescalar.py)  # Ejecuta el script de Python y lee el tiempo de ejecución
    resultados+=("$tiempo")
    echo "Resultado de la iteración $((i+1)): $tiempo"
done



