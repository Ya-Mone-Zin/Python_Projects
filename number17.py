import pandas as pd
import statsmodels.api as sm

# Load your data
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Selecting your independent (predictor) variables and dependent variable
# Example: Using SCT as the dependent variable and various environmental factors as independent variables
X = near_miss_data[['RESIDENTIAL', 'BUSINESS', 'RURAL', 'TRAFFIC_LOW', 'TRAFFIC_MID', 'TRAFFIC_HIGH']]
y = near_miss_data['SCT']  # or 'TTC'

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the multiple regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression
print(model.summary())
