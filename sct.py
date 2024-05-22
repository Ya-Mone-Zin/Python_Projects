import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Compute the descriptive statistics for SCT
sct_descriptive_stats = near_miss_data['SCT'].describe(percentiles=[.25, .5, .75])
print(sct_descriptive_stats)

# Draw the histogram for SCT
plt.figure(figsize=(10, 6))
plt.hist(near_miss_data['SCT'], bins='auto', color='skyblue', edgecolor='black')
plt.title('Histogram of Vehicle Safety Margin (SCT)')
plt.xlabel('Safety Margin (SCT)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
