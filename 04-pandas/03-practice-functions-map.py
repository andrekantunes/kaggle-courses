# Practice 3 - Summary Functions and Maps

import pandas as pd
import numpy as np

pd.set_option('max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews)

# Question 1 -
# Median of points

median_points = reviews.points.median()
print(median_points)

# Question 2 -
# List of the countries in dataset (without duplicates)
countries = reviews.country.unique()
print(countries)

# Question 3 -
# Count each country
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)

# Question 4 -
# Centered Price - Price - Mean Price
centered_price = reviews.price - reviews.price.mean()
print(centered_price)

# Question 5 -
# Best bargain (ratio points to price)
bargain_idx = (reviews.points/reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine)

# Question 6 -
# Descriptor count how many times words appear
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

print(n_trop)
print(n_fruity)
print(descriptor_counts)

# Question 7 -
# Create series star rating
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)
