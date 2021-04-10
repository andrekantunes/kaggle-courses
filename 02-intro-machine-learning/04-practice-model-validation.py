# Practice 4 - Model Validation

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Path of the file to read
iowa_file_path = '../kaggle-datasets/03-home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit Model
iowa_model.fit(X, y)

print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

# Question 1 -
# Splitting Data

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Question 2 -
# Specify and Fit the model

iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)

# Question 3 -
# Make predictions with validation data

val_predictions = iowa_model.predict(val_X)
# print(val_predictions[0:5])
# print(val_y[0:5])

# Question 4 - 
# Calculate MAE - Mean Absolute Error

mean_abs_error = mean_absolute_error(val_y, val_predictions)
print(mean_abs_error)
print(home_data.describe())