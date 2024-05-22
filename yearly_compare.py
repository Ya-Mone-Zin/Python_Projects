import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Filter the data for the years 2006 to 2021
filtered_data = near_miss_data[(near_miss_data['YEAR'] >= 2006) & (near_miss_data['YEAR'] <= 2021)]

# Group the data by year and calculate average speeds for VCAR and V_OBJ using a list
yearly_average_speeds = filtered_data.groupby('YEAR')[['VCAR', 'V_OBJ']].mean()

# Plotting the yearly average speeds
plt.figure(figsize=(12, 6))
plt.plot(yearly_average_speeds['VCAR'], marker='o', label='Average Vehicle Approach Speed')
plt.plot(yearly_average_speeds['V_OBJ'], marker='o', label='Average Cyclist Speed')
plt.title('Yearly Average Vehicle and Cyclist Approach Speeds (2006-2021)')
plt.xlabel('Year')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.show()
