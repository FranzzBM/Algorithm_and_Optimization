import math
import random
import matplotlib.pyplot as plt

cities = {i: (random.uniform(0, 100), random.uniform(0, 100)) for i in range(20)}

def tour_length(route):
    return sum(math.dist(cities[route[i]], cities[route[(i + 1) % len(route)]]) for i in range(len(route)))

def two_opt_move(route, i, k):
    return route[:i] + route[i:k + 1][::-1] + route[k + 1:]

def two_opt_search(route):
    improvements = 0
    best_length = tour_length(route)
    best_route = route
    
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for k in range(i + 1, len(route)):
                new_route = two_opt_move(best_route, i, k)
                new_length = tour_length(new_route)
                if new_length < best_length:
                    best_route = new_route
                    best_length = new_length
                    improvements += 1
                    improved = True
                    break
            if improved:
                break
    return best_route, best_length, improvements

n_runs = 30
improvements_random, lengths_random = [], []
improvements_nn, lengths_nn = [], []

for _ in range(n_runs):
    random_route = list(cities.keys())
    random.shuffle(random_route)
    _, final_len_rand, num_imp_rand = two_opt_search(random_route)
    improvements_random.append(num_imp_rand)
    lengths_random.append(final_len_rand)
    
    start_node = random.choice(list(cities.keys()))
    unvisited = set(cities.keys()) - {start_node}
    nn_route = [start_node]
    current = start_node
    while unvisited:
        next_node = min(unvisited, key=lambda x: math.dist(cities[current], cities[x]))
        nn_route.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    _, final_len_nn, num_imp_nn = two_opt_search(nn_route)
    improvements_nn.append(num_imp_nn)
    lengths_nn.append(final_len_nn)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.boxplot([improvements_random, improvements_nn], labels=['Random Start', 'NN Start'])
ax1.set_title('Number of 2-opt Improvements to Converge')
ax1.set_ylabel('Number of Swaps')
ax1.grid(True, axis='y')

ax2.boxplot([lengths_random, lengths_nn], labels=['Random Start', 'NN Start'])
ax2.set_title('Quality of Local Optimum (Final Cost)')
ax2.set_ylabel('Tour Length (Lower is better)')
ax2.grid(True, axis='y')

plt.tight_layout()
plt.show()