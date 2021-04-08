### Lesson 3 - First Machine Learning Model

# Selecting data for modeling

import pandas as pd

# Import csv data into dataframe with read_csv from panda library
melbourne_file_path = 'data/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

# Show summary from the dataframe
# print(melbourne_data.describe())

# Print columns of the Dataframe
print(melbourne_data.columns)

# Drop missing values
melbourne_data = melbourne_data.dropna(axis=0)

# Show summary from the dataframe
print(melbourne_data.describe())


### Select Subset of Data

### Prediction Target

# Select single column - convention y
y = melbourne_data.Price

# print(y)

### Chosing Features - columns are called features - convention X
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# print(melbourne_features)
print(X.describe())
print(X.head())


### Building a Model

# The steps to building and using a model are:

# Define: What type of model will it be? 
# A decision tree? Some other type of model? Some other parameters of the model type are specified too.

# Fit: Capture patterns from provided data. This is the heart of modeling.

# Predict: Just what it sounds like

# Evaluate: Determine how accurate the model's predictions are.

### Library scikit-learn (sklearn) to create models

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model - X (Features) and y (Target) // Training
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())

print("The predictions are")
print(melbourne_model.predict(X.head()))