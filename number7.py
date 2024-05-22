import pandas as pd

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Calculate the median of SCT
sct_median = near_miss_data['SCT'].median()

# Divide the data into two datasets based on the median of SCT
dataset_1 = near_miss_data[near_miss_data['SCT'] < sct_median]
dataset_2 = near_miss_data[near_miss_data['SCT'] >= sct_median]

# Optionally, you can print the number of records in each dataset to verify the split
print(f"Number of records in Dataset 1 (SCT < median): {dataset_1.shape[0]}")
print(f"Number of records in Dataset 2 (SCT >= median): {dataset_2.shape[0]}")
