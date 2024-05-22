import pandas as pd
import statsmodels.api as sm

# Load your data
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Creating Dataset 2
sct_median = near_miss_data['SCT'].median()
dataset_2 = near_miss_data[near_miss_data['SCT'] >= sct_median]

# Replace with your chosen environmental factors
X = dataset_2[['RESIDENTIAL', 'TRAFFIC_HIGH', 'YGAP']]  # Example choices
Y = dataset_2['VCAR']

# Add a constant to the model
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(Y, X).fit()

# Print the summary of the regression
print(model.summary())
