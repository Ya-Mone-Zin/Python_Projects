import datetime
import matplotlib.pyplot as plt

# Data stream with temperatures and corresponding timestamps
data_stream = [
    ('1:1:0', 17.06), ('1:1:1', 16.26), ('1:1:2', 15.18),
    ('1:1:3', 17.73), ('1:1:3', 16.87), # Assuming there are two readings at '1:1:3'
    ('1:1:4', 18.19), # Current time
    ('1:1:5', 14.87), ('1:1:6', 17.87)
]

# Function to convert timestamp to seconds past the hour
def timestamp_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

# Function to calculate the average temperature in a window
def calculate_average(data, current_time, window_size):
    window_data = [temp for time, temp in data if current_time - window_size < time <= current_time]
    if window_data:
        return round(sum(window_data) / len(window_data), 2)
    else:
        return 0

# Initialize variables
window_size = 4  # 4 seconds window
slide_size = 2   # 2 seconds slide
current_time_str = '1:1:4'
current_time = timestamp_to_seconds(current_time_str)

# Convert data stream to seconds
data_stream_seconds = [(timestamp_to_seconds(time), temp) for time, temp in data_stream]

# Calculate the average temperature at the current time and then every 2 seconds using data from the past 4 seconds
averages = [(current_time_str, calculate_average(data_stream_seconds, current_time, window_size))]
for _ in range(2):  # Assuming we want to calculate for the next two slides as an example
    current_time += slide_size
    current_average = calculate_average(data_stream_seconds, current_time, window_size)
    averages.append((str(datetime.timedelta(seconds=current_time)), current_average))

# Plot the results
times = [timestamp_to_seconds(t) for t, _ in averages]
temps = [temp for _, temp in averages]
plt.plot(times, temps, marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Average Temperature')
plt.title('Average Temperature Over 4s Window Every 2s')
plt.grid(True)
plt.show()
