# Lesson 6 - Random Forest

# Decision trees leave you with a difficult decision. 
# A deep tree with lots of leaves will overfit because each prediction is coming
# from historical data from only the few houses at its leaf.
# 
# But a shallow tree with few leaves will perform poorly because it fails to
# capture as many distinctions in the raw data.

# The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree.
# It generally has much better predictive accuracy than a single decision tree and it works well with default parameters.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
    
# Load data
melbourne_file_path = '../kaggle-datasets/02-melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

# Filter rows with missing values
melbourne_data = melbourne_data.dropna(axis=0)

# Choose target and features
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)


# Specify the model
forest_model = RandomForestRegressor(random_state=1)

# Fit the model
forest_model.fit(train_X, train_y)