#!/bin/bash

# Definir el número de iteraciones
num_iteraciones=5
resultados=()

# Iterar sobre el script de Python y almacenar los resultados
for ((i=0; i<num_iteraciones; i++)); do
    tiempo=$(python3 2vectorScalarMultiply.py)  # Ejecuta el script de Python y lee el tiempo de ejecución
    resultados+=("$tiempo")
    echo "Resultado de la iteración $((i+1)): $tiempo"
done

# Ordenar los resultados de menor a mayor
IFS=$'\n' sorted_resultados=($(sort -n <<<"${resultados[*]}"))

# Imprimir solo los tres resultados más pequeños (excluyendo el primero y el último)
echo "Tres resultados más pequeños (excluyendo el primero y el último):"
for ((i=1; i<num_iteraciones-1 && i<=3; i++)); do
    echo "${sorted_resultados[i]}"
done

# Calcular el promedio de los tres resultados más pequeños
suma=0
for ((i=1; i<num_iteraciones-1 && i<=3; i++)); do
    suma=$(awk "BEGIN {print $suma + ${sorted_resultados[i]}}")
done
promedio=$(awk "BEGIN {printf \"%.15f\", $suma / 3}")



