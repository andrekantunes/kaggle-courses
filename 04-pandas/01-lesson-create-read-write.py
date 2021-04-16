# Lesson 1 - Create, Read and Write

import pandas as pd

# Creating Data

# DataFrames
# Table containg arrays of values

# Dataframe with integers
test_data_int = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(test_data_int)

# Dataframe with strings
test_data_strings = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(test_data_strings)

# Dataframe with labeled rows - Product A will be the name of the row
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

# Series
# List of values (One row dataframe)
# Don't have column name
test_list_int = pd.Series([1, 2, 3, 4, 5])
print(test_list_int)

test_list_label = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(test_list_label)

# Reading data files
# wine_reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv")
# print(wine_reviews.shape)
# print(wine_reviews.head())

# Using the first column as index
# wine_reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
# print(wine_reviews.shape)
# print(wine_reviews.head())



