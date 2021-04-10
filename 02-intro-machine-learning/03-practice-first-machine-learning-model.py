### Practice 3 - First Machine Learning Model

# Import libraries
import pandas as pd

# Path of the file to read
iowa_file_path = '../kaggle-datasets/03-home-data-for-ml-course/train.csv'

# .csv to dataframe
home_data = pd.read_csv(iowa_file_path)

### Question 1 -

# Especify prediction target

# Print the list of columns
print(home_data.columns)

#Save the prediction target to variable y
y = home_data.SalePrice
# print(y)

### Question 2 -

# Especify the features

home_features = [
    "LotArea",
    "YearBuilt",
    "1stFlrSF",
    "2ndFlrSF",
    "FullBath",
    "BedroomAbvGr",
    "TotRmsAbvGrd"
]

X = home_data[home_features]

# print(X)

### Question 3 -

# Specify and Fit the model

# Import scikit learn library
# DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor

# Define the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model // Training
iowa_model.fit(X, y)

### Question 4 - 

# Make predictions

predictions = iowa_model.predict(X)
print(predictions)

# Compare results

# Results
print(y.head())

# Predictions
print(predictions[0:5])