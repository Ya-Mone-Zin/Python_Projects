import pandas as pd
from scipy.stats import ttest_ind

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Calculate the median of SCT
sct_median = near_miss_data['SCT'].median()

# Create Dataset 1 (SCT < median) and Dataset 2 (SCT >= median)
dataset_1 = near_miss_data[near_miss_data['SCT'] < sct_median]
dataset_2 = near_miss_data[near_miss_data['SCT'] >= sct_median]

# Perform an independent t-test to check for statistical difference in VCAR between the two datasets
ttest_result = ttest_ind(dataset_1['VCAR'], dataset_2['VCAR'], equal_var=False)

print(f"T-test result: {ttest_result}")
