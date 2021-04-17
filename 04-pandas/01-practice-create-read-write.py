# Practice 1 - Create, Read and Write

import pandas as pd

# Question 1 -
# Create a dataframe

# fruits = pd.DataFrame({ 'Apples': [30], 'Bananas': [21]})
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
print(fruits)

# Question 2 -
# Create fruit sales dataframe

#fruits = pd.DataFrame({ 'Apples': [35, 41], 'Bananas': [21,34]}, index=['2017 Sales', '2018 Sales'])
fruits = pd.DataFrame([[35, 21], [41, 34]], 
                columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
print(fruits)

# Question 3 - 
# Series ingredients

# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object

# ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
ingredients = pd.Series(quantities, index=items, name='Dinner')

print(ingredients)

# Question 4 -
# Reading dataframe

reviews = pd.read_csv("../kaggle-datasets/06-wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())

# Question 5 -
# Animals dataframe

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)

# Writing to csv

animals.to_csv("01-submission.csv")