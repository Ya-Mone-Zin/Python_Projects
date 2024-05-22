import pandas as pd

# Load the data from the CSV file
near_miss_data_path = '/Users/yamonezin/python/near_miss_data.csv'
near_miss_data = pd.read_csv(near_miss_data_path)

near_miss_data['Total_Distance'] = near_miss_data['DBLIND'] + near_miss_data['DOBJ']

# Calculate descriptive statistics for VCAR
v_car_stats = near_miss_data['VCAR'].describe(percentiles=[.25, .5, .75])

# Calculate descriptive statistics for Total_Distance
total_distance_stats = near_miss_data['Total_Distance'].describe(percentiles=[.25, .5, .75])

# Calculate descriptive statistics for V_OBJ
v_obj_stats = near_miss_data['V_OBJ'].describe(percentiles=[.25, .5, .75])

# Display the results
print("Descriptive Statistics for Vehicle Speed (VCAR):")
print(v_car_stats)

print("\nDescriptive Statistics for Total Remaining Distance (DBLIND + DOBJ):")
print(total_distance_stats)

print("\nDescriptive Statistics for Cyclist Speed (V_OBJ):")
print(v_obj_stats)


