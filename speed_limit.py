import pandas as pd

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Count the number of instances where vehicle speed (VCAR) exceeds the speed limit (VLIM)
speed_limit_exceeded_count = near_miss_data[near_miss_data['VCAR'] > near_miss_data['VLIM']].shape[0]

print(f"Number of instances where the vehicle speed exceeds the speed limit: {speed_limit_exceeded_count}")
