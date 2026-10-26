import math
import random
import matplotlib.pyplot as plt
import time

cities = {i: (random.uniform(0, 100), random.uniform(0, 100)) for i in range(25)}

def tour_length(route):
    return sum(math.dist(cities[route[i]], cities[route[(i + 1) % len(route)]]) for i in range(len(route)))

def two_opt_random_move(route):
    i = random.randint(1, len(route) - 3)
    k = random.randint(i + 1, len(route) - 1)
    return route[:i] + route[i:k + 1][::-1] + route[k + 1:]

def simulated_annealing(route, schedule_func, max_iter=3000):
    current_route = route
    current_len = tour_length(route)
    history = [current_len]
    
    for t in range(1, max_iter):
        T = schedule_func(t, max_iter)
        if T <= 0.001: break
        
        next_route = two_opt_random_move(current_route)
        next_len = tour_length(next_route)
        delta_E = current_len - next_len
        
        if delta_E > 0 or random.random() < math.exp(delta_E / T):
            current_route = next_route
            current_len = next_len
        history.append(current_len)
        
    return current_route, current_len, history

def linear_cool(t, max_t, T0=100):
    return T0 * (1 - t/max_t)

def exp_cool(t, max_t, T0=100, alpha=0.995):
    return T0 * (alpha ** t)

n_runs = 15
time_lin, cost_lin = [], []
time_exp, cost_exp = [], []

sample_hist_lin = None
sample_hist_exp = None

for _ in range(n_runs):
    initial_route = list(cities.keys())
    random.shuffle(initial_route)
    
    t0 = time.perf_counter()
    _, final_len, hist_l = simulated_annealing(initial_route, linear_cool)
    time_lin.append(time.perf_counter() - t0)
    cost_lin.append(final_len)
    sample_hist_lin = hist_l
    
    t0 = time.perf_counter()
    _, final_len, hist_e = simulated_annealing(initial_route, exp_cool)
    time_exp.append(time.perf_counter() - t0)
    cost_exp.append(final_len)
    sample_hist_exp = hist_e

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(sample_hist_lin, label='Linear Cooling')
ax1.plot(sample_hist_exp, label='Exponential Cooling')
ax1.set_title('Convergence Curves (Single Run)')
ax1.set_xlabel('Iterations')
ax1.set_ylabel('Cost')
ax1.legend()
ax1.grid(True)

ax2.scatter(time_lin, cost_lin, color='blue', label='Linear', alpha=0.7)
ax2.scatter(time_exp, cost_exp, color='orange', label='Exponential', alpha=0.7)
ax2.set_title('Execution Time vs Final Solution Quality')
ax2.set_xlabel('Execution Time (seconds)')
ax2.set_ylabel('Final Tour Length (Lower is better)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()