### Practice 2 - Basic Data Exploration

# Question 1 -
# Loading data into dataframe

import pandas as pd

# Path of the file to read
iowa_file_path = 'data/home-data-train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Question 2 -
# View Summary of the data

print(home_data.describe())
