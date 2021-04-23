# Practice 4 - Grouping and sorting

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews)
# print(reviews.describe())
print(reviews.columns)

# Question 1 -
# Who are the most common wine reviewers in the dataset?
# Create a `Series` whose index is the `taster_twitter_handle` category from the dataset,
# and whose values count how many reviews each person wrote.

reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
# reviews_written = reviews.groupby('taster_twitter_handle').size()
print(reviews_written)

# Question 2 -
# What is the best wine I can buy for a given amount of money?
# Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing
# that much was given in a review. Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).

best_rating_per_price = reviews.groupby('price').points.max().sort_index(ascending=True)
# best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)

# Question 3 -
# What are the minimum and maximum prices for each `variety` of wine?
# Create a `DataFrame` whose index is the `variety` category from the dataset
# and whose values are the `min` and `max` values thereof.

price_extremes = reviews.groupby('variety')['price'].agg([min, max])
print(price_extremes)

# Question 4 -
# What are the most expensive wine varieties? Create a variable sorted_varieties
# containing a copy of the dataframe from the previous question where varieties
# are sorted in descending order based on minimum price, then on maximum price (to break ties).

sorted_varieties = reviews.groupby('variety')['price'].agg([min, max]).sort_values(by=['min', 'max'], ascending=False).copy()
# sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
print(sorted_varieties)

# Question 5 -
# Create a `Series` whose index is reviewers and whose values is the average review score given out by that reviewer.
# Hint: you will need the `taster_name` and `points` columns.

reviewer_mean_ratings = reviews.groupby('taster_name')['points'].agg(np.mean)
# reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
print(reviewer_mean_ratings)

# Question 6 -
# What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof {country, variety} pairs.
# For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. Sort the values in the Series in descending order based on wine count.

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
print(country_variety_counts)
