# Exercise 1: Parallel Speedup

Este ejercicio estima el valor de π con el método Monte Carlo y compara el tiempo de ejecución secuencial con el paralelo.

## Funcionamiento

La función `estimate_pi` genera puntos aleatorios dentro del cuadrado unitario y calcula qué proporción cae dentro del cuarto de círculo. Multiplica esa proporción por 4 para obtener la estimación de π. El programa procesa ocho semillas y compara la ejecución secuencial con grupos de 1, 2, 4 y 8 procesos.

La aceleración se calcula como el tiempo secuencial dividido por el tiempo paralelo. Al final, se muestra en consola la aceleración de cada cantidad de procesos y un gráfico que la compara con la aceleración ideal.

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
python parallel_speedup.py
```

El tiempo y la aceleración pueden variar según el equipo y la carga del sistema.
