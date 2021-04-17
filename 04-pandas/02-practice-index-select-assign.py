# Practice 2 - Indexing, Selecting and Assigning

import pandas as pd

reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

# Question 1 -
# Select description column and assing to variable desc

# desc = reviews["description"] 
desc = reviews.description
print(type(desc))
print(desc)

# Question 2 -
# Select First Value of reviews

# first_description = reviews["description"][0]
# first_description = reviews.description[0]
# first_description = reviews.description.loc[0]
first_description = reviews.description.iloc[0]
print(first_description)

# Question 3 -
# Select first row of data
first_row = reviews.iloc[0]
print(first_row)

# Question 4 -
# Select 10 first values
# first_descriptions = reviews["description"][0:10]
first_descriptions = reviews.description.iloc[:10]
print(first_descriptions)

# Question 5 -
# Select records and assign to varable
# first_descriptions = reviews["description"][0:10]
first_descriptions = reviews.iloc[[1, 2, 3, 5, 8]]
print(first_description)

# Question 6 - 
# Records
df = reviews.loc[ [ 0, 1, 10, 100], 
                    ["country", "province", "region_1", "region_2"]]

# Question 7 - 
# First 100 rows of Country and Variety

# Loc include first exclude last                 
df = reviews.loc[:99,["country", "variety"]]

# Iloc require numeric values for columns
# df = reviews.iloc[ :100, [0, 11]]
print(df)            

# Question 8 - 
# Italian wines made in italy
italian_wines = reviews.loc[reviews.country == "Italy"]
print(italian_wines)

# Question 9 -
# Top Oceania Wines at least 95 points (Australia or New Zealand)
top_oceania_wines = reviews.loc[((reviews.country == "Australia") |
                                (reviews.country == "New Zealand")) &
                                (reviews.points >= 95) ]
print(top_oceania_wines)