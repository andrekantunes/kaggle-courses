# Lesson 4 - Grouping and sorting

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews)

# Groupby analysis
print(reviews.groupby('points').points.count())
print(reviews.groupby('points').price.min())

print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))