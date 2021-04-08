# Titanic Challenge -

### Goal

# Predict if a passenger survived the sinking of the Titanic or not.
# For each in the test set, you must predict a 0 or 1 value for the variable.

### Metric

# Your score is the percentage of passengers you correctly predict. This is known as accuracy.

### Submission File Format

# You should submit a csv file with exactly 418 entries plus a header row.
# Your submission will show an error if you have extra columns (beyond PassengerId and Survived) or rows.

# The file should have exactly 2 columns:

# PassengerId (sorted in any order)
# Survived (contains your binary predictions: 1 for survived, 0 for deceased)

import pandas
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

### load .csv into dataframes

train_data = pandas.read_csv("train.csv")
test_data = pandas.read_csv("test.csv")

# Clear NaN values of the Dataframe
train_data = train_data.dropna(axis=0)

### Show the number of rows of the dataframe

print("Train colums: ", train_data.columns.tolist())
print("Test colums: ", test_data.columns.tolist())

# Describe summary of the data
# print(train_data.describe())

# Using DecisionTreeRegression

# Set prediction target
y = train_data.Survived
# print(y)

# Choosing features
titanic_features = ["Age", "SibSp", "Fare"]
X = train_data[titanic_features]
print(X)

# Define model
titanic_model = DecisionTreeRegressor(random_state=1)

# Fit model - X (Features) and y (Target)
titanic_model.fit(X, y)

# Compare train values and predictions - Results 10/10
print(train_data[0:10])
print(titanic_model.predict(X[0:10]))

# Splitting the data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Fit the model with training data
titanic_model.fit(train_X, train_y)

# Obtain predictions with the model built on the values of X splitted
val_predictions = titanic_model.predict(val_X)
mean_abs_error_splitted = mean_absolute_error(val_y, val_predictions)

print(mean_abs_error_splitted)


# # AGE

# # Remove rows containg NaN in column "Age"
# train_data_age_clean = train_data.dropna(subset=['Age'])
# # print(train_data_age_clean)

# # Show the number of rows of the dataframe
# print(len(train_data.index) - len(train_data_age_clean.index),
#       "columns containing NaN removed")

# # Keep the rows where the value of Survived equal to 1
# age_survived = train_data_age_clean[train_data_age_clean.Survived == 1]
# age_sorted = age_survived.sort_values(by=['Age'], ascending=True)
# #print(age_sorted)

# age_survived = age_survived.groupby("Age", sort=True)["Survived"].sum()
# #print(age_survived)

# seaborn.barplot(x='Age', y='Survived', data=train_data_age_clean)