# Practice 6 - Renaming and Combining

import pandas as pd

pd.set_option('display.max_rows', 5)
reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)

print(reviews.head)

# Question 1 -
# Rename columns `region_1` and `region_2` Create a copy of `reviews`
# with these columns renamed to `region` and `locale`, respectively.
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})
print(renamed.columns)

# Question 2 -
# Rename index with wines
reindexed = reviews.rename_axis("wines", axis='rows')
print(reindexed)

# Question 3 -
# Create a dataframe with products mentioned on either subreddit
gaming_products = pd.read_csv("../kaggle-datasets/08-things-on-reddit/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../kaggle-datasets/08-things-on-reddit/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

combined_products = pd.concat([gaming_products, movie_products])
print(combined_products)

# Question 4 -
# Both tables include references to a `MeetID`, a unique key for each meet (competition) included in the database. Using this, generate a dataset combining the two tables into one.

powerlifting_meets = pd.read_csv("../kaggle-datasets/09-powerlifting/meets.csv")
powerlifting_competitors = pd.read_csv("../kaggle-datasets/09-powerlifting/openpowerlifting.csv")

left = powerlifting_meets.set_index('MeetID')
right = powerlifting_competitors.set_index('MeetID')

powerlifting_combined = left.join(right, lsuffix='meets', rsuffix='competitors')

# powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
print(powerlifting_combined)