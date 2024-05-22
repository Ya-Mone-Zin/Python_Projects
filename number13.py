import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the dataset
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Create Dataset 1 based on SCT median
sct_median = near_miss_data['SCT'].median()
dataset_1 = near_miss_data[near_miss_data['SCT'] < sct_median]

# Selecting independent variables (example: 'RESIDENTIAL', 'BUSINESS', 'RURAL', 'YGAP') and dependent variable 'VCAR'
X = dataset_1[['RESIDENTIAL', 'BUSINESS', 'RURAL', 'YGAP']]  # Add or remove variables as needed
y = dataset_1['VCAR']

# Adding a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression
print(model.summary())

summary = model.summary2().tables[1]

df_stats = pd.DataFrame({
    'Coefficients': summary['Coef.'],
    'Standard Errors': summary['Std.Err.'],
    't-values': summary['t'],
    'p-values': summary['P>|t|']
})

df_stats = df_stats.drop('const')

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=df_stats.index, y='Coefficients', data=df_stats)
plt.errorbar(x=df_stats.index, y=df_stats['Coefficients'], yerr=df_stats['Standard Errors'], fmt='o', color='black')
plt.title('Regression Coefficients with Standard Errors')
plt.xlabel('Variables')
plt.ylabel('Coefficients')
plt.xticks(rotation=45)
plt.show()
