### Lesson 2 - Basic Data Exploration

# The panda library

import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../kaggle-datasets/02-melbourne-housing-snapshot/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melbourne data
# count - non empty rows
# mean, standard deviation and min, quarters and max
print(melbourne_data.describe())

# print all data
# print(melbourne_data)