# Lesson 6 - XGBoost

# Build and optimize models with gradient boosting.

# Gradient boosting is a method that goes through cycles
# to iteratively add models into an ensemble.

# It begins by initializing the ensemble with a single model,
# whose predictions can be pretty naive. 
# 
# (Even if its predictions are wildly inaccurate, subsequent additions
#  to the ensemble will address those errors.)

# The cycle:

# First, we use the current ensemble to generate predictions for each observation in the dataset.
# To make a prediction, we add the predictions from all models in the ensemble.
#
# These predictions are used to calculate a loss function (like mean squared error, for instance).
#
# Then, we use the loss function to fit a new model that will be added to the ensemble.
# Specifically, we determine model parameters so that adding this new model to the ensemble
# will reduce the loss. 
# 
# (Side note: The "gradient" in "gradient boosting" refers to the fact that we'll use gradient
# descent on the loss function to determine the parameters in this new model.)
#
# Finally, we add the new model to ensemble, and ...
# ... repeat!

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv('../kaggle-datasets/02-melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

# Import XGBoost Library
from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)

# Predictions to evaluate the model
from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))

# Parameter tunning


# n_estimators


#  specifies how many times to go through the modeling cycle described above.
# It is equal to the number of models that we include in the ensemble.

# Too low a value causes underfitting, which leads to inaccurate predictions
# on both training data and test data.
#
# Too high a value causes overfitting, which causes accurate predictions on training data,
# but inaccurate predictions on test data (which is what we care about).

# my_model = XGBRegressor(n_estimators=500)
# my_model.fit(X_train, y_train)


# early_stopping_rounds


# early_stopping_rounds offers a way to automatically find the ideal value for n_estimators.
# Early stopping causes the model to stop iterating when the validation score stops improving,
# even if we aren't at the hard stop for n_estimators.
# 
# It's smart to set a high value for n_estimators and then use early_stopping_rounds
# to find the optimal time to stop iterating.

# Since random chance sometimes causes a single round where validation scores don't improve,
# you need to specify a number for how many rounds of straight deterioration to allow before stopping.


# learning_rate


# This means each tree we add to the ensemble helps us less

# In general, a small learning rate and large number of estimators will yield more accurate XGBoost models,
# though it will also take the model longer to train since it does more iterations through the cycle.
# As default, XGBoost sets learning_rate=0.1.


# n_jobs

# Large sets of data, using the cores of your machine
# Number of cores

my_model = XGBRegressor(n_estimators=500, learning_rate=0.05, n_jobs=12)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)],
             verbose=False)