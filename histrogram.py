import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Calculate the total remaining distance as the sum of DBLIND and DOBJ
near_miss_data['Total_Distance'] = near_miss_data['DBLIND'] + near_miss_data['DOBJ']

# Histogram for Vehicle Approach Speed (VCAR)
plt.figure(figsize=(10, 6))
plt.hist(near_miss_data['VCAR'], bins='auto', color='blue', alpha=0.7)
plt.title('Histogram of Vehicle Approach Speed (VCAR)')
plt.xlabel('VCAR (km/h)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram for Total Remaining Distance (DBLIND + DOBJ)
plt.figure(figsize=(10, 6))
plt.hist(near_miss_data['Total_Distance'], bins='auto', color='green', alpha=0.7)
plt.title('Histogram of Total Remaining Distance (DBLIND + DOBJ)')
plt.xlabel('Total Distance (m)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram for Cyclist Approach Speed (V_OBJ)
plt.figure(figsize=(10, 6))
plt.hist(near_miss_data['V_OBJ'], bins='auto', color='red', alpha=0.7)
plt.title('Histogram of Cyclist Approach Speed (V_OBJ)')
plt.xlabel('V_OBJ (km/h)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
