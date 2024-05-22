import pandas as pd

# Load the data from the CSV file
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Check the unique values in the 'BRIGHTNESS' column
unique_brightness_values = near_miss_data['BRIGHTNESS'].unique()
print("Unique values in the 'BRIGHTNESS' column:", unique_brightness_values)
