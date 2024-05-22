import matplotlib.pyplot as plt

# Data stream with timestamps and prices
data_stream = [
    ('1:1:0', 17.06), ('1:1:1', 16.26), ('1:1:2', 15.18),
    ('1:1:7', 17.73), ('1:1:9', 16.87), ('1:1:10', 18.19), 
    ('1:1:13', 14.87), ('1:1:20', 17.87), ('1:1:23', 15.97), 
    ('1:1:29', 17.32), ('1:1:31', 18.21), ('1:1:34', 19.91), 
    ('1:1:40', 16.57), ('1:1:46', 16.57), ('1:1:52', 14.98), 
    ('1:1:55', 16.56), ('1:1:58', 17.86), ('1:1:60', 15.86), 
    ('1:1:66', 19.16), ('1:1:72', 18.95), ('1:1:77', 17.21), 
    ('1:1:79', 16.57), ('1:1:82', 18.87), ('1:1:82', 18.87)
]

# Function to convert timestamp to seconds
def timestamp_to_seconds(timestamp):
    h, m, s = map(int, timestamp.split(':'))
    return h * 3600 + m * 60 + s

# Function to identify session windows
def find_session_windows(data_stream, session_boundary):
    session_windows = []
    current_window = []
    last_timestamp = -1
    
    for timestamp, value in data_stream:
        seconds = timestamp_to_seconds(timestamp)
        if last_timestamp >= 0 and seconds - last_timestamp > session_boundary:
            # Save the current window and start a new one
            session_windows.append(current_window)
            current_window = []
        current_window.append(value)
        last_timestamp = seconds
        
    # Don't forget to save the last window
    if current_window:
        session_windows.append(current_window)
    
    return session_windows

# Function to find the maximum price in each session window
def max_price_in_windows(session_windows):
    return [max(window) if window else 0 for window in session_windows]

# Session boundary is set to 4 seconds
session_boundary = 4
session_windows = find_session_windows(data_stream, session_boundary)
max_prices = max_price_in_windows(session_windows)

# Plotting the maximum prices for each window
plt.figure(figsize=(10, 6))
plt.plot(max_prices, marker='o', linestyle='-', color='blue')
plt.title('Maximum Price in Each Session Window')
plt.xlabel('Window Number')
plt.ylabel('Maximum Price')
plt.grid(True)
plt.show()
