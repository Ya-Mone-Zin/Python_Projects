import heapq
import matplotlib.pyplot as plt

# Given data stream
data_stream = [('1:1:0', 147.87), ('1:1:1', 146.98), ('1:1:2', 148.18), 
               ('1:1:3', 147.73), ('1:1:4', 148.19), ('1:1:15', 146.87), 
               ('1:1:6', 147.97), ('1:1:7', 149.97), ('1:1:8',148.21) ]

# Convert timestamps to a comparable format (e.g., seconds)
def timestamp_to_seconds(timestamp):
    h, m, s = map(int, timestamp.split(':'))
    return h * 3600 + m * 60 + s

# Initialize a min heap for the memory
memory = []

# Function to handle the memory constraint
def handle_memory(memory, new_element):
        if len(memory) < 5:
            heapq.heappush(memory, new_element)
        else:
        # Replace the smallest element if the new one is larger
            if new_element > memory[0]:
                heapq.heapreplace(memory, new_element)

def compute_average(heap):
    return sum(heap) / len(heap) if heap else 0

def get_minimum(heap):
    return heap[0] if heap else None

averages = {}
minimums = {}

for timestamp, rate in data_stream:
    seconds = timestamp_to_seconds(timestamp)
    handle_memory(memory, rate)

    # Compute the average
    averages[timestamp] = sum(memory) / len(memory) if memory else 0
    # Find the minimum
    minimums[timestamp] = memory[0] if memory else None

# Plotting the results
times = [timestamp_to_seconds(t) for t, _ in data_stream]
avg_rates = [averages[t] for t, _ in data_stream]
min_rates = [minimums[t] for t, _ in data_stream]

plt.figure(figsize=(10, 5))
plt.plot(times, avg_rates, marker='o', linestyle='-', color='blue', label='Average Rate')
plt.scatter(times, min_rates, color='red', label='Minimum Rate')
plt.xlabel('Time (seconds from start)')
plt.ylabel('Exchange Rate')
plt.title('Exchange Rate Analysis')
plt.legend()
plt.grid(True)
plt.xticks(times, [t for t, _ in data_stream])
plt.show()
