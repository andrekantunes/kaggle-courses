# Lesson 3 - Parsing Dates

import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# Read data
landslides = pd.read_csv("../kaggle-datasets/13-landslides/catalog.csv")
print(landslides.head())

# print the first few rows of the date column
print(landslides['date'].head())

# check the data type of our date column
print(landslides['date'].dtype)

# create a new column, date_parsed, with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")

# print the first few rows
print(landslides['date_parsed'].head())

# get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
print(day_of_month_landslides.head())

# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()

# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)