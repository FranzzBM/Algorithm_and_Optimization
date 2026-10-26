# Algorithms and Optimization

## Español

### Acerca del proyecto

Este proyecto reúne cinco ejercicios en Python sobre algoritmos y técnicas de optimización. Cada ejercicio explora un problema o método diferente y presenta los resultados en la consola o mediante gráficos.

### Estructura

```text
Algorithm_and_Optimization/
├── Exercise 1 - Parallel Speedup/
│   ├── parallel_speedup.py
│   └── README.md
├── Exercise 2 - Greedy Knapsack/
│   ├── greedy_knapsack.py
│   └── README.md
├── Exercise 3 - Local Search/
│   ├── local_search.py
│   └── README.md
├── Exercise 4 - Parameter Tuning/
│   ├── parameter_tuning.py
│   └── README.md
├── Exercise 5 - Aproximation Ratio/
│   ├── aproximation_ratio.py
│   └── README.md
└── README.md
```

### ¿Qué contiene cada ejercicio?

1. **Parallel Speedup:** estima π con Monte Carlo y compara la ejecución secuencial y paralela.
2. **Greedy Knapsack:** compara dos estrategias voraces para seleccionar objetos en el problema de la mochila.
3. **Local Search:** aplica búsqueda local 2-opt al problema del viajante y compara diferentes rutas iniciales.
4. **Parameter Tuning:** compara calendarios de enfriamiento para el recocido simulado aplicado al problema del viajante.
5. **Aproximation Ratio:** compara varios métodos para el problema del viajante y mide la razón de aproximación de una solución basada en un árbol de expansión mínima.

Cada carpeta contiene el código del ejercicio y un README con instrucciones y detalles específicos.

### Requisitos generales

- Python 3.8 o posterior.
- Matplotlib para generar los gráficos.

Instala Matplotlib con:

```bash
python -m pip install matplotlib
```

Para ejecutar un ejercicio, abre una terminal en su carpeta y ejecuta el script correspondiente, por ejemplo:

```bash
python parallel_speedup.py
```

Consulta el README de cada ejercicio para más información. Los experimentos aleatorios pueden producir resultados diferentes en cada ejecución.

## English

### About the project

This project brings together five Python exercises about algorithms and optimization techniques. Each exercise explores a different problem or method and presents its results in the console or through charts.

### Project structure

```text
Algorithm_and_Optimization/
├── Exercise 1 - Parallel Speedup/
│   ├── parallel_speedup.py
│   └── README.md
├── Exercise 2 - Greedy Knapsack/
│   ├── greedy_knapsack.py
│   └── README.md
├── Exercise 3 - Local Search/
│   ├── local_search.py
│   └── README.md
├── Exercise 4 - Parameter Tuning/
│   ├── parameter_tuning.py
│   └── README.md
├── Exercise 5 - Aproximation Ratio/
│   ├── aproximation_ratio.py
│   └── README.md
└── README.md
```

### What does each exercise contain?

1. **Parallel Speedup:** estimates π using Monte Carlo and compares sequential and parallel execution.
2. **Greedy Knapsack:** compares two greedy strategies for selecting items in the knapsack problem.
3. **Local Search:** applies 2-opt local search to the traveling salesperson problem and compares different initial routes.
4. **Parameter Tuning:** compares cooling schedules for simulated annealing applied to the traveling salesperson problem.
5. **Aproximation Ratio:** compares several methods for the traveling salesperson problem and measures the approximation ratio of a solution based on a minimum spanning tree.

Each folder contains the exercise code and a README with specific details and instructions.

### General requirements

- Python 3.8 or later.
- Matplotlib for generating charts.

Install Matplotlib with:

```bash
python -m pip install matplotlib
```

To run an exercise, open a terminal in its folder and run the corresponding script, for example:

```bash
python parallel_speedup.py
```

See each exercise's README for more information. Randomized experiments may produce different results each time they are run.
