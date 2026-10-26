# Exercise 2: Greedy Knapsack

Este ejercicio compara dos estrategias voraces para seleccionar objetos en una instancia del problema de la mochila 0/1.

## Funcionamiento

La función `knapsack_greedy` ordena los objetos según el criterio recibido y agrega cada objeto si cabe en la capacidad restante. El ejemplo compara:

- **Valor/peso:** prioriza objetos con mayor valor por unidad de peso.
- **Menor peso:** prioriza los objetos más livianos.

El programa imprime los objetos seleccionados, el peso utilizado y el valor total de cada método. También muestra un gráfico comparativo. La instancia de prueba está definida en el código y tiene capacidad máxima de 10.

Una estrategia voraz es una heurística: para el problema de mochila 0/1 no garantiza encontrar la solución óptima en todas las instancias.

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
python greedy_knapsack.py
```
