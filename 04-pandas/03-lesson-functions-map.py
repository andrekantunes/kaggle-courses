# Lesson 3 - Summary Functions and Maps

import pandas as pd
import numpy as np

pd.set_option('max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews)

# Summary Functions
print(reviews.describe())
print(reviews.points.describe())
print(reviews.taster_name.describe())

# Mean
print(reviews.points.mean())

# Unique
print(reviews.taster_name.unique())

# Count values
print(reviews.taster_name.value_counts())

# Maps
review_points_mean = reviews.points.mean()
print(reviews.points)
review_points_std = reviews.points.map(lambda p: p - review_points_mean)
print(review_points_std)

# Apply
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

# reviews.apply(remean_points, axis='columns')
# reviews.apply(remean_points, axis='index')
# print(reviews)

# map() and apply() return new, transformed Series and DataFrames, respectively
print(reviews.head(1))

# remeaning values
review_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)

# All values - one value
# All values - all values (with series of same length)
print(reviews.country + " - " + reviews.region_1)