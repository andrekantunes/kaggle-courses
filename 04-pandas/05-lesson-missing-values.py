# Lesson 5 - Data types and missing values

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# DTypes
print(reviews.price.dtype)
print(reviews.dtypes)

# Transform data type astype
print(reviews.points.astype('float64'))

# Type of index
print(reviews.index.dtype)

# Missing data
# NaN - Not a Number - float64

# Country is NaN
print(reviews[pd.isnull(reviews.country)])

# Fill NaN values with fillna
print(reviews.region_2.fillna("Unknown"))

# Replace values
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))