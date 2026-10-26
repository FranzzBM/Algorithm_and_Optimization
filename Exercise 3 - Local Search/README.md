# Exercise 3: Local Search

Este ejercicio aplica búsqueda local 2-opt al problema del viajante (TSP) y compara dos formas de construir la ruta inicial.

## Funcionamiento

El programa genera 20 ciudades con coordenadas aleatorias. Para cada prueba compara:

- **Inicio aleatorio:** baraja el orden de las ciudades.
- **Vecino más cercano:** comienza en una ciudad aleatoria y agrega repetidamente la ciudad no visitada más cercana.

La búsqueda 2-opt invierte segmentos de la ruta mientras encuentra una ruta de menor longitud. Se ejecutan 30 pruebas por estrategia y se muestran diagramas de caja del número de mejoras y de la longitud final de las rutas. Una longitud menor representa una ruta más corta.

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
python local_search.py
```

Las ciudades, las rutas iniciales y los resultados dependen de valores aleatorios, por lo que pueden cambiar entre ejecuciones.
