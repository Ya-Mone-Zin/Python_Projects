import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt


# Function to simulate SIR model with initial seed nodes
def SIR_simulation_with_seeds(G, seed_nodes, infection_rate, recovery_rate):
    status = {node: 0 for node in G.nodes()}  # 0: S, 1: I, 2: R
    for node in seed_nodes:
        status[node] = 1  # Initial seed nodes are 'Infected'

    while any(s == 1 for s in status.values()):  # While there are infected nodes
        new_status = status.copy()
        for node in G.nodes():
            if status[node] == 1:  # If the node is infected
                if random.random() < recovery_rate:
                    new_status[node] = 2  # Recovered
                for neighbor in G.neighbors(node):
                    if status[neighbor] == 0 and random.random() < infection_rate:
                        new_status[neighbor] = 1  # Infected
        status = new_status

    return sum(s == 2 for s in status.values())  # Count nodes in state R

# Function to select seed nodes based on strategy
def choose_seed_nodes(G, strategy, k):
    if strategy == 'high-degree':
        return [n for n, d in sorted(G.degree(), key=lambda x: x[1], reverse=True)[:k]]
    elif strategy == 'high-betweenness':
        betweenness = nx.betweenness_centrality(G)
        return sorted(betweenness, key=betweenness.get, reverse=True)[:k]
    elif strategy == 'combined':
        top_degree = [n for n, d in sorted(G.degree(), key=lambda x: x[1], reverse=True)[:k // 2]]
        betweenness = nx.betweenness_centrality(G)
        top_betweenness = sorted(betweenness, key=betweenness.get, reverse=True)[:k // 2]
        return top_degree + top_betweenness
    elif strategy == 'random':
        return random.sample(list(G.nodes()), k)

# Parameters
infection_rate = 0.05
recovery_rate = 1.0
num_simulations = 100
k_values = [5, 10, 15]  # Different numbers of seed nodes

# Create a network (Replace with network from your data)
G = nx.erdos_renyi_graph(100, 0.1)

# Run simulations
results = {}
for k in k_values:
    for strategy in ['high-degree', 'high-betweenness', 'combined', 'random']:
        R_values = []
        for _ in range(num_simulations):
            seed_nodes = choose_seed_nodes(G, strategy, k)
            R = SIR_simulation_with_seeds(G, seed_nodes, infection_rate, recovery_rate)
            R_values.append(R)
        results[(strategy, k)] = np.mean(R_values)

# Create a graph
plt.figure(figsize=(10, 6))
for strategy in ['high-degree', 'high-betweenness', 'combined', 'random']:
    avg_R = [results[(strategy, k)] for k in k_values]
    plt.plot(k_values, avg_R, label=strategy, marker='o')

plt.title("Average R per Strategy and Seed Node Count")
plt.xlabel("Number of Seed Nodes (k)")
plt.ylabel("Average R")
plt.legend()
plt.grid(True)
plt.show()
