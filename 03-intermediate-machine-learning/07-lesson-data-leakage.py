# Lesson 7 - Data Leakage

# Data leakage (or leakage) happens when your training data contains information about the target,
# but similar data will not be available when the model is used for prediction. 
# This leads to high performance on the training set (and possibly even the validation data),
# but the model will perform poorly in production.

# In other words, leakage causes a model to look accurate until you start making
# decisions with the model, and then the model becomes very inaccurate.


# Target Leakage

# To prevent this type of data leakage, any variable updated (or created)
# after the target value is realized should be excluded.

# Train test contamination

# When you aren't careful to distinguish training data from validation data.

# Recall that validation is meant to be a measure of how the model does on data that it hasn't considered before.
# You can corrupt this process in subtle ways if the validation data affects the preprocessing behavior.
# This is sometimes called train-test contamination.

# For example, imagine you run preprocessing (like fitting an imputer for missing values) before calling train_test_split().
# The end result? Your model may get good validation scores, giving you great confidence in it,
# but perform poorly when you deploy it to make decisions.

import pandas as pd

# Read the data
data = pd.read_csv('../kaggle-datasets/05-aer-credit-card-data/AER_credit_card_data.csv', 
                   true_values = ['yes'], false_values = ['no'])

# Select target
y = data.card

# Select predictors
X = data.drop(['card'], axis=1)

print("Number of rows in the dataset:", X.shape[0])
X.head()

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Since there is no preprocessing, we don't need a pipeline (used anyway as best practice!)
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, 
                            cv=5,
                            scoring='accuracy')

print("Cross-validation accuracy: %f" % cv_scores.mean())

expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]

print('Fraction of those who did not receive a card and had no expenditures: %.2f' \
      %((expenditures_noncardholders == 0).mean()))
print('Fraction of those who received a card and had no expenditures: %.2f' \
      %(( expenditures_cardholders == 0).mean()))      