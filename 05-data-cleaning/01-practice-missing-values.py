# Practice 1 - Handling missing values

import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("../kaggle-datasets/11-building-permits/Building_Permits.csv")
                      
# set seed for reproducibility
np.random.seed(0) 

# Question 1 -
# Take a first look at the data

# Print first 5 rows
print(sf_permits.head())

# Question 2 -
# How many missing points

# Columns with missing values
missing_columns = sf_permits.isnull().sum()

# Percent missing
total = np.product(sf_permits.shape)
missing = missing_columns.sum()

percent_missing = missing / total * 100
print(percent_missing)

# Question 3 -
# Why data is missing

# Street Number Suffix missing likely because it doesnt exist
# Zipcode missing likely it was not recorded

# Question 4 -
# Drop missing values (rows)
sf_permits_dropna = sf_permits.dropna()
print(sf_permits_dropna)

# Question 5 -
# Drop missing values (columns)
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

print("Columns in original dataset: %d \n" % sf_permits.shape[1])
print("Columns with na's dropped: %d" % sf_permits_with_na_dropped.shape[1])

# Question 6 -
# Fill in missing values
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)
print(sf_permits_with_na_imputed)