# Exercise 5: MST Aproximation

Este ejercicio compara varios métodos para el problema del viajante (TSP) y mide la razón de aproximación de una ruta construida a partir de un árbol de expansión mínima (MST).

## Funcionamiento

El programa genera 100 instancias aleatorias de nueve ciudades. Para cada instancia calcula la ruta óptima mediante fuerza bruta y compara:

- **MST:** construye un árbol de expansión mínima con Prim y visita sus nodos en preorden.
- **MST + 2-opt:** mejora la ruta del MST mediante búsqueda local 2-opt.
- **Búsqueda local:** aplica 2-opt a una ruta inicial aleatoria.
- **Recocido simulado:** explora rutas desde una ruta inicial aleatoria con enfriamiento exponencial.

La razón de aproximación del MST se calcula como el costo de su ruta dividido por el costo óptimo. El programa muestra un histograma de esas razones, junto con una referencia teórica en 2, y diagramas de caja para comparar los costos finales. Una ruta de menor costo es mejor.

El cálculo óptimo por fuerza bruta es costoso; este experimento limita cada instancia a nueve ciudades.

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
python mst_aproximation.py
```

Las instancias y los resultados dependen de valores aleatorios, por lo que pueden variar entre ejecuciones.
