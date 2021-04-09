# Practice 5 - Underfitting and Overfitting

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'data/home-data-train.csv'

home_data = pd.read_csv(iowa_file_path)

# Create target object and call it y
y = home_data.SalePrice

# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

# Function get MAE
def get_mae(max_leafs, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leafs, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

# Question 1 -
# Compare different tree sizes

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

# for leafs in candidate_max_leaf_nodes:
#     my_mae = get_mae(leafs, train_X, val_X, train_y, val_y)
#     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(leafs, my_mae))

# Create a dictionary to keep the values { leaf_size: MAE}
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
print(scores)

best_tree_size = min(scores, key=scores.get)
print(best_tree_size)

# Question 2 -
# Fit model using all data

# If you were going to deploy this model in practice, you would make it even more accurate by using all of the data and keeping that tree size.
# That is, you don't need to hold out the validation data now that you've made all your modeling decisions.

# Fill in argument to make optimal size 100
final_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=0)

# fit the final model with all data
final_model.fit(X, y)