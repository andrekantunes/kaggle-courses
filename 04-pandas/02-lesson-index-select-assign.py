# Lesson 2 - Indexing, Selecting e Assigning

import pandas as pd

reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)


# Native accessors


print(reviews)

print(reviews.country)

print(reviews["country"])

print(reviews["country"][0])


# Indexing pandas


# 1 - Index-based selection
# Select data in numeric position (row-first, column-second)

# Select First row
print(reviews.iloc[0])

# Select first column
print(reviews.iloc[:, 0])

# Select first 3 rows and column
print(reviews.iloc[:3, 0])

# Select 2 and 3 entries
print(reviews.iloc[1:3, 0])

# Passing a list of parameters
print(reviews.iloc[[0, 1, 2], 0])

# Negative numbers, starting by the end of the values
print(reviews.iloc[-5:])


# Label-based selection

print(reviews.loc[0, 'country'])

# Loc (use index) - iLoc (ignore index, include first exclude last)

print(reviews.loc[:, ["taster_name", "taster_twitter_handle", "points"]])


# Manipulating the Index


print(reviews.set_index("title"))

# Conditional selecting
print(reviews.country == "Italy")

# Use conditional inside a loc
print(reviews.loc[reviews.country == "Italy"])

# Choose italian wine and above average 90 -100
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])

# Italian or above 90
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

# Select wines from Italy and France only ( Is in )
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])

# Is null and Is not null - isnull and notnull
# Filter values which are not on the data or empty
print(reviews.loc[reviews.price.notnull()])


# Assigning data

# Assign a constant
reviews['critic'] = 'everyone'
print(reviews["critic"])

# Assign a iterable value

reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])