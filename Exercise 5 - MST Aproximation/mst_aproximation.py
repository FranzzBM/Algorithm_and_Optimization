import itertools
import math
import random
import matplotlib.pyplot as plt

def mst_prim(points):
    best = {v: (math.dist(points[0], points[v]), 0) for v in range(1, len(points))}
    children = {v: [] for v in range(len(points))}
    while best:
        v = min(best, key=lambda u: best[u][0])
        children[best.pop(v)[1]].append(v)
        for u in best:
            d = math.dist(points[v], points[u])
            if d < best[u][0]:
                best[u] = (d, v)
    return children

def preorder(children, root=0):
    return [root] + [c for child in children[root] for c in preorder(children, child)]

def tour_length(points, tour):
    return sum(math.dist(points[tour[i]], points[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

def local_search_2opt(points, route):
    improved = True
    best_route = route
    best_length = tour_length(points, route)
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for k in range(i + 1, len(best_route)):
                new_route = best_route[:i] + best_route[i:k+1][::-1] + best_route[k+1:]
                nl = tour_length(points, new_route)
                if nl < best_length:
                    best_route, best_length = new_route, nl
                    improved = True
                    break
            if improved: break
    return best_length

def simulated_annealing(points, route, max_iter=2000):
    current_route = route
    current_len = tour_length(points, route)
    T0 = 100
    for t in range(1, max_iter):
        T = T0 * (0.99 ** t)
        if T <= 0.001: break
        
        i = random.randint(1, len(route) - 3)
        k = random.randint(i + 1, len(route) - 1)
        next_route = current_route[:i] + current_route[i:k+1][::-1] + current_route[k+1:]
        next_len = tour_length(points, next_route)
        
        delta_E = current_len - next_len
        if delta_E > 0 or random.random() < math.exp(delta_E / T):
            current_route = next_route
            current_len = next_len
    return current_len

n_cities = 9
n_instances = 100

ratios_mst = []
costs_mst = []
costs_mst_2opt = []
costs_ls = []
costs_sa = []

for _ in range(n_instances):
    points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(n_cities)]
    random_tour = list(range(n_cities))
    random.shuffle(random_tour)
    
    opt_tour = min(((0,) + p for p in itertools.permutations(range(1, len(points)))), 
                key=lambda t: tour_length(points, t))
    cost_opt = tour_length(points, opt_tour)
    
    mst_tour = preorder(mst_prim(points))
    cost_mst = tour_length(points, mst_tour)
    ratios_mst.append(cost_mst / cost_opt)
    costs_mst.append(cost_mst)
    
    costs_mst_2opt.append(local_search_2opt(points, mst_tour))
    
    costs_ls.append(local_search_2opt(points, random_tour))
    
    costs_sa.append(simulated_annealing(points, random_tour))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.hist(ratios_mst, bins=15, color='orange', edgecolor='black')
ax1.axvline(x=2.0, color='red', linestyle='dashed', linewidth=2, label='Theoretical Limit (2)')
ax1.set_title('Approximation Ratio Distribution (MST)')
ax1.set_xlabel('Ratio ($C_{obtained} / C_{optimal}$)')
ax1.set_ylabel('Frequency')
ax1.legend()

data_to_plot = [costs_mst, costs_mst_2opt, costs_ls, costs_sa]
labels = ['Pure MST', 'MST + 2-opt', 'Local Search\n(Random Start)', 'Sim. Annealing\n(Random Start)']

ax2.boxplot(data_to_plot, labels=labels)
ax2.set_title('Final Cost Comparison of Algorithmic Approaches')
ax2.set_ylabel('Total Tour Distance (Lower is better)')
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()