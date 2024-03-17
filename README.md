
##  Profiling en Python y C con instrucciones AVX

- Univalle
- Curso: Infraestructuras Paralelas y Distribuidas
- Profesor: Jhon Alexander Sanabria Ordoñez
- Estudiantes:
  - Herney Eduardo Quintero Trochez

### 1. Instalar las dependencias de python del archivo requirements.txt

```bash
bash install.sh
```

### 1. Ejecutar el script para compilar la librearía en C 

```bash
bash compile.sh
```

### Para ejectuar el profiling con timeit
```bash
cd src
bash timeit.sh
```

### Para ejectuar el profiling con cProfile
```bash
cd src
bash cprofile.sh
```