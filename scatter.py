import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Create a scatter plot of VCAR and V_OBJ
plt.figure(figsize=(10, 6))
sns.scatterplot(x='VCAR', y='V_OBJ', data=near_miss_data)
plt.title('Scatter Plot of Vehicle Approach Speed (VCAR) vs Cyclist Speed (V_OBJ)')
plt.xlabel('Vehicle Approach Speed (VCAR)')
plt.ylabel('Cyclist Speed (V_OBJ)')
plt.show()

# Calculate the correlation coefficient
correlation_coefficient = near_miss_data['VCAR'].corr(near_miss_data['V_OBJ'])
print(f"Correlation Coefficient: {correlation_coefficient}")


