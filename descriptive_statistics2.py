import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Calculate the median of SCT
sct_median = near_miss_data['SCT'].median()

# Create Dataset 2: SCT >= median
dataset_2 = near_miss_data[near_miss_data['SCT'] >= sct_median]

# Compute the descriptive statistics for VCAR in Dataset 2
vcar_dataset_2_stats = dataset_2['VCAR'].describe(percentiles=[.25, .5, .75])
print(vcar_dataset_2_stats)

# Draw the histogram for VCAR in Dataset 2
plt.figure(figsize=(10, 6))
plt.hist(dataset_2['VCAR'], bins='auto', color='green', alpha=0.7)
plt.title('Histogram of Vehicle Approach Speed (VCAR) in Dataset 2')
plt.xlabel('Vehicle Approach Speed (VCAR)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
