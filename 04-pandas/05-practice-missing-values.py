# Practice 5 - Data types and missing values

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Question 1 -
# Type of Points Data
dtype = reviews.points.dtype
print(dtype)

# Question 2 -
# Series of points - to string
point_strings = reviews.points.astype('str')
print(point_strings)

# Question 3 -
# How many null prices in the reviews
n_missing_prices = reviews.price.isnull().sum()
# n_missing_prices = pd.isnull(reviews.price).sum()
print(n_missing_prices)

# Question 4 -
# What are the most common wine-producing regions?
# Create a Series counting the number of times each value occurs in the `region_1` field.
# This field is often missing data, so replace missing values with `Unknown`. Sort in descending order.
reviews_per_region = reviews.fillna("Unkown").groupby('region_1')['region_1'].count().sort_values(ascending=False)
# reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)