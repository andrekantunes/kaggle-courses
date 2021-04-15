# Lesson 5 - Cross Validation

# Better measures of model performance

# In cross-validation, we run our modeling process on different
# subsets of the data to get multiple measures of model quality.

# For example, we could begin by dividing the data into 5 pieces, each 20% of the full dataset.
# In this case, we say that we have broken the data into 5 "folds".
# run one experiment for each fold

# For small datasets, where extra computational burden isn't a big deal, you should run cross-validation.
# 
# For larger datasets, a single validation set is sufficient. Your code will run faster,
# and you may have enough data that there's little need to re-use some of it for holdout.

import pandas as pd

# Read the data
data = pd.read_csv('../kaggle-datasets/02-melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

# Define pipeline and model

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                            ])

# Cross validation scores

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)                             

print("Average MAE score (across experiments):")
print(scores.mean())