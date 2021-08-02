# Practice 3 - Parsing Dates

import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# Read data
landslides = pd.read_csv("../kaggle-datasets/13-landslides/catalog.csv")
print(landslides.head())

# set seed for reproducibility
np.random.seed(0)

# Question 1 -
# Check data type of date
print(landslides['date'].dtype)

# Question 2 -
# Convert date to datetime
print(landslides['date'].head())

landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")
print(landslides['date'].head())

# Question 3 -
# Get the day of the month

# get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
print(day_of_month_landslides.head())

# Question 4 -
# Plot Day of the Month

# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()

# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)