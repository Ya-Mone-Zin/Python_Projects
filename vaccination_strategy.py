import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

# Function to apply SIR model on a network
def SIR_simulation(G, initial_infected, vaccinated_nodes, infection_rate, recovery_rate):
    # Initialize states: S: 0, I: 1, R: 2
    status = {node: 0 for node in G.nodes()}
    for node in vaccinated_nodes:
        status[node] = 2  # Vaccinated nodes are 'Recovered'
    status[initial_infected] = 1  # Initial infected node

    # Track the spread over time
    S, I, R = [len(G.nodes()) - len(vaccinated_nodes)], [1], [len(vaccinated_nodes)]

    while I[-1] > 0:
        new_status = status.copy()
        for node in G.nodes():
            if status[node] == 1:  # Infected
                # Recovery process
                if random.random() < recovery_rate:
                    new_status[node] = 2  # Recovered
                else:
                    # Infection process
                    neighbors = list(G.neighbors(node))
                    for neighbor in neighbors:
                        if status[neighbor] == 0 and random.random() < infection_rate:
                            new_status[neighbor] = 1  # Infected
        status = new_status
        S.append(sum(1 for n in status if status[n] == 0))
        I.append(sum(1 for n in status if status[n] == 1))
        R.append(sum(1 for n in status if status[n] == 2))

    return S, I, R

# Function to choose nodes for vaccination
def choose_vaccination_nodes(G, strategy, k):
    if strategy == 'high-degree':
        nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)[:k]
        return [node[0] for node in nodes]  # Extracting node numbers from (node, degree) tuples
    elif strategy == 'high-betweenness':
        betweenness = nx.betweenness_centrality(G)
        nodes = sorted(betweenness, key=betweenness.get, reverse=True)[:k]
        return list(nodes)  # Directly returning the list of node numbers
    elif strategy == 'combined':
        top_degree = sorted(G.degree, key=lambda x: x[1], reverse=True)[:k//2]
        top_degree_nodes = [node[0] for node in top_degree]
        betweenness = nx.betweenness_centrality(G)
        top_betweenness_nodes = sorted(betweenness, key=betweenness.get, reverse=True)[:k//2]
        return top_degree_nodes + top_betweenness_nodes  # Combining the two lists of node numbers
    elif strategy == 'random':
        return random.sample(list(G.nodes()), k)  # Convert G.nodes() to a list


# Example usage
G = nx.erdos_renyi_graph(100, 0.1)  # Creating a random graph
k = 10  # Number of nodes to vaccinate
infection_rate = 0.05
recovery_rate = 0.1
initial_infected = random.choice(list(G.nodes()))

strategies = ['high-degree', 'high-betweenness', 'combined', 'random']
results = {}

for strategy in strategies:
    vaccinated_nodes = choose_vaccination_nodes(G, strategy, k)
    S, I, R = SIR_simulation(G, initial_infected, vaccinated_nodes, infection_rate, recovery_rate)
    results[strategy] = (S, I, R)

# Plotting the results
plt.figure(figsize=(12, 8))
for strategy in strategies:
    S, I, R = results[strategy]
    plt.plot(S, label=f'{strategy} - Susceptible')
    plt.plot(I, label=f'{strategy} - Infected')
    plt.plot(R, label=f'{strategy} - Recovered')

plt.xlabel('Time steps')
plt.ylabel('Number of nodes')
plt.title('SIR Model Simulation with Different Vaccination Strategies')
plt.legend()
plt.show()
