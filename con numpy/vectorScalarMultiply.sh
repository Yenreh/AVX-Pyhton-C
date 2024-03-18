#!/bin/bash

# Definir el número de iteraciones
num_iteraciones=5
resultados_primera_porcion=()
resultados_segunda_porcion=()

# Iterar sobre el script de Python y almacenar los resultados de la primera y segunda porción
for ((i=0; i<num_iteraciones; i++)); do
    tiempos=$(python3 vectorScalarMultiply.py)  # Ejecuta el script de Python y lee los tiempos de ejecución
    resultado_primera=$(echo "$tiempos" | awk 'NR==1{print}')  # Extraer el tiempo de la primera porción
    resultado_segunda=$(echo "$tiempos" | awk 'NR==2{print}')  # Extraer el tiempo de la segunda porción
    resultados_primera_porcion+=("$resultado_primera")
    resultados_segunda_porcion+=("$resultado_segunda")
    echo "Resultado de la iteración $((i+1)) - Primera porción: $resultado_primera, Segunda porción: $resultado_segunda"
done

# Ordenar los resultados de menor a mayor para ambas porciones
IFS=$'\n' sorted_resultados_primera_porcion=($(sort -n <<<"${resultados_primera_porcion[*]}"))
IFS=$'\n' sorted_resultados_segunda_porcion=($(sort -n <<<"${resultados_segunda_porcion[*]}"))

# Imprimir solo los tres resultados más pequeños de la primera porción (excluyendo el primero y el último)
echo "Tres resultados más pequeños de la primera porción (excluyendo el primero y el último):"
for ((i=1; i<num_iteraciones-1 && i<=3; i++)); do
    echo "${sorted_resultados_primera_porcion[i]}"
done

# Imprimir solo los tres resultados más pequeños de la segunda porción (excluyendo el primero y el último)
echo "Tres resultados más pequeños de la segunda porción (excluyendo el primero y el último):"
for ((i=1; i<num_iteraciones-1 && i<=3; i++)); do
    echo "${sorted_resultados_segunda_porcion[i]}"
done



