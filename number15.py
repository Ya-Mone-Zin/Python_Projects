import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Choosing relevant variables for regression
X = near_miss_data[['RESIDENTIAL', 'TRAFFIC_HIGH', 'TIME16_20', 'YGAP']]  # Example features
y = near_miss_data['SCT']  # Assuming SCT is continuous

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Example regression model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
