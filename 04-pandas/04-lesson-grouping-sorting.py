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
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))
print(reviews.groupby(['country']).price.agg([len, min, max]))

# Multi indexing
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

mi = countries_reviewed.index
type(mi)

print(countries_reviewed.reset_index())

# Sorting
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))

# Ascending e Descending
print(countries_reviewed.sort_values(by='len', ascending=False))

print(countries_reviewed.sort_index())

# Sort by more than a column
print(countries_reviewed.sort_values(by=['country', 'len']))
