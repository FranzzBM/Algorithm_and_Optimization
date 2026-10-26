import matplotlib.pyplot as plt

def knapsack_greedy(items, values, weights, W, key_func):
    data = sorted(zip(items, values, weights), key=lambda x: key_func(x), reverse=True)
    
    capacity = W
    total_value = 0
    selected_items = []
    
    for item, v, w in data:
        if w <= capacity:
            selected_items.append(item)
            total_value += v
            capacity -= w
            
    return selected_items, W - capacity, total_value

items = ["A", "B", "C"]
values = [1, 100, 10]
weights = [1, 10, 5]
max_capacity = 10

res_vw = knapsack_greedy(items, values, weights, max_capacity, key_func=lambda x: x[1]/x[2])

res_weight = knapsack_greedy(items, values, weights, max_capacity, key_func=lambda x: -x[2])

print(f"{'Method':<20} | {'Selected Items':<15} | {'Used Capacity':<15} | {'Total Value':<10}")
print("-" * 68)
print(f"{'Value/Weight Ratio':<20} | {str(res_vw[0]):<15} | {res_vw[1]:<15} | {res_vw[2]:<10}")
print(f"{'Lowest Weight First':<20} | {str(res_weight[0]):<15} | {res_weight[1]:<15} | {res_weight[2]:<10}")

labels = ['Value/Weight Method', 'Lowest Weight Method']
total_values = [res_vw[2], res_weight[2]]
used_capacities = [res_vw[1], res_weight[1]]

x = range(len(labels))
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar([pos - 0.2 for pos in x], total_values, width=0.4, label='Total Value', color='forestgreen')
ax.bar([pos + 0.2 for pos in x], used_capacities, width=0.4, label='Used Capacity', color='slategray')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_title('Greedy Knapsack: Value/Weight vs Lowest Weight Priority')
ax.legend()
plt.show()