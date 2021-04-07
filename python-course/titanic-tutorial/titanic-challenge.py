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
import seaborn

### load .csv into dataframes

train_data = pandas.read_csv("train.csv")
test_data = pandas.read_csv("test.csv")

### Show the number of rows of the dataframe

print("Train colums: ", train_data.columns.tolist())
print("Test colums: ", test_data.columns.tolist())

# AGE

# Remove rows containg NaN in column "Age"
train_data_age_clean = train_data.dropna(subset=['Age'])
# print(train_data_age_clean)

# Show the number of rows of the dataframe
print(len(train_data.index) - len(train_data_age_clean.index),
      "columns containing NaN removed")

# Keep the rows where the value of Survived equal to 1
age_survived = train_data_age_clean[train_data_age_clean.Survived == 1]
age_sorted = age_survived.sort_values(by=['Age'], ascending=True)
#print(age_sorted)

age_survived = age_survived.groupby("Age", sort=True)["Survived"].sum()
#print(age_survived)

seaborn.barplot(x='Age', y='Survived', data=train_data_age_clean)