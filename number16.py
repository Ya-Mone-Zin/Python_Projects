import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
near_miss_data = pd.read_csv('/Users/yamonezin/python/near_miss_data.csv')

# Choose your features and target variable
X = near_miss_data[['RESIDENTIAL', 'TRAFFIC_HIGH', 'TIME16_20', 'YGAP']]  # Example features
y = near_miss_data['SCT']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Regressor
dtree_model = DecisionTreeRegressor(random_state=42)

# Fit the model to the training data
dtree_model.fit(X_train, y_train)

# Predict on the test data
y_pred = dtree_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)
