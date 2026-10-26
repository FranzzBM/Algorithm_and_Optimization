import multiprocessing as mp
import random
import time
import matplotlib.pyplot as plt

def estimate_pi(seed: int, samples: int = 1_000_000) -> float:
    rng = random.Random(seed)
    inside = sum(rng.random()**2 + rng.random()**2 <= 1.0 for _ in range(samples))
    return 4 * inside / samples

if __name__ == "__main__":
    seeds = list(range(8))
    process_counts = [1, 2, 4, 8]
    speedups = []

    t0 = time.perf_counter()
    [estimate_pi(s) for s in seeds]
    t_seq = time.perf_counter() - t0

    for processes in process_counts:
        t0 = time.perf_counter()
        with mp.Pool(processes=processes) as pool:
            pool.map(estimate_pi, seeds)
        t_par = time.perf_counter() - t0
        
        speedup = t_seq / t_par
        speedups.append(speedup)
        print(f"Processes: {processes}, Speedup: {speedup:.2f}x")

    plt.figure(figsize=(8, 5))
    plt.plot(process_counts, speedups, marker='o', label='Actual Speedup', color='blue')
    plt.plot(process_counts, process_counts, linestyle='--', label='Ideal Speedup', color='red')
    plt.title('Parallel Speedup vs. Number of Processes')
    plt.xlabel('Number of Processes')
    plt.ylabel('Speedup')
    plt.xticks(process_counts)
    plt.legend()
    plt.grid(True)
    plt.show()