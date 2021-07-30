# Lesson 1 - Handling missing values

import pandas as pd
import numpy as np

# Read Data
nfl_data = pd.read_csv("../kaggle-datasets/10-nfl-plays/NFL Play by Play 2009-2016 (v3).csv",
                      low_memory=False)

# Set random seed
np.random.seed(0)

# Look at first rows
print(nfl_data.head())

# Number of missing values
missing_count = nfl_data.isnull().sum()

# Look at missing values
print(missing_count[0:10])

# Total of missing values
total_cells = np.product(nfl_data.shape)
total_missing = missing_count.sum()

# Percent of missing data
percent_missing = total_missing / total_cells * 100
print(percent_missing)

# Drop missing values
nfl_data.dropna()

# remove all columns with at least one missing value
columns_with_na_dropped = nfl_data.dropna(axis=1)
print(columns_with_na_dropped.head())

# just how much data did we lose?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# Finding missing values automatically

# get a small subset of the NFL dataset
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()
print(subset_nfl_data)

# replace all NA's with 0
# subset_nfl_data = subset_nfl_data.fillna(0)
print(subset_nfl_data)

# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
subset_nfl_data = subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)
print(subset_nfl_data)