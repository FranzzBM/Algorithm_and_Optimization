# Exercise 4: Simulated Annealing

Este ejercicio compara dos calendarios de enfriamiento para el recocido simulado aplicado al problema del viajante (TSP).

## Funcionamiento

El programa genera 25 ciudades y busca rutas más cortas mediante movimientos 2-opt aleatorios. El algoritmo acepta siempre una mejora y puede aceptar una ruta peor con una probabilidad que depende de la temperatura.

Se comparan los siguientes calendarios:

- **Lineal:** reduce la temperatura linealmente desde un valor inicial de 100.
- **Exponencial:** reduce la temperatura multiplicándola por `0.995` en cada iteración.

Se realizan 15 ejecuciones por calendario, con un máximo de 3.000 iteraciones. Se muestran curvas de convergencia de una ejecución de cada método y un gráfico de tiempo de ejecución frente a longitud final para las pruebas. Una longitud menor indica una ruta de menor costo.

## Requisitos

- Python 3.8 o posterior.
- Matplotlib.

Instala Matplotlib si aún no está disponible:

```bash
python -m pip install matplotlib
```

## Ejecución

Desde esta carpeta, ejecuta:

```bash
python simulated_annealing.py
```

Las ciudades, las rutas iniciales y los resultados dependen de valores aleatorios.
