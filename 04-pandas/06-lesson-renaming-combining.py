# Lesson 6 - Renaming and Combining

import pandas as pd

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Renaming columns
# changing points to score
print(reviews.rename(columns={'points': 'score'}))

# Renaming rows (index)
print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))

print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

# Combining
# Concat, merge, join

# Concat
# Data in different dataframes having the same fields - columns
canadian_youtube = pd.read_csv("../kaggle-datasets/07-youtube-trending/CAvideos.csv")
korean_youtube = pd.read_csv("../kaggle-datasets/07-youtube-trending/KRvideos.csv")

print(canadian_youtube.shape)
print(korean_youtube.shape)
print(pd.concat([canadian_youtube, korean_youtube]).shape)

# Join
# Combine different data with index in common
left = canadian_youtube.set_index(['title', 'trending_date'])
right = korean_youtube.set_index(['title', 'trending_date'])

print(left.join(right, lsuffix='_CAN', rsuffix='_KR'))