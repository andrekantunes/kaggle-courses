### Lesson 4 - Model Validation

# There are many metrics for summarizing model quality, but we'll start with one called
# Mean Absolute Error (also called MAE)
# Error = Actual - Prediction

# If a house cost $150,000 and you predicted it would cost $100,000 the error is $50,000.

# Absolute value of each error (positive number)
# Take the average of those absolute errors.

# On average, our predictions are off by about X.

# Model

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load data
melbourne_file_path = '../kaggle-datasets/02-melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

# Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)

# Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

# Define model
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

# Calculate Mean Absolute Error
predicted_home_prices = melbourne_model.predict(X)
mean_abs_error = mean_absolute_error(y, predicted_home_prices)

print(mean_abs_error)

# Measure performance on data that wasn't used to build the model.
# Exclude some data from the model-building process,
# and then use those to test the model's accuracy on data it hasn't seen before.
# 
#  This data is called validation data.
#
# Splitting the data

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Define model
# melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit the model with training data
melbourne_model.fit(train_X, train_y)

# Obtain predictions with the model built on the values of X splitted
val_predictions = melbourne_model.predict(val_X)
mean_abs_error_splitted = mean_absolute_error(val_y, val_predictions)

print(mean_abs_error_splitted)

# Compare the mean value with the absoulte error 1.000.000,00 with 262.494.30 (25%)
print(val_y.describe())
