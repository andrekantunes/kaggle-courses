# Practice 3 - Categorical Variables

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# Read the data
X = pd.read_csv('../kaggle-datasets/03-home-data-for-ml-course/train.csv', index_col='Id')
X_test = pd.read_csv('../kaggle-datasets/03-home-data-for-ml-course/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll drop columns with missing values
cols_with_missing = [col for col in X.columns if X[col].isnull().any()] 
X.drop(cols_with_missing, axis=1, inplace=True)
X_test.drop(cols_with_missing, axis=1, inplace=True)

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                      train_size=0.8, test_size=0.2,
                                                      random_state=0)

print(X_train.head())                                                      

# function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Question 1 -
# Drop Categorical data

drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

print("MAE from Approach 1 (Drop categorical variables):")
print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))

print("Unique values in 'Condition2' column in training data:", X_train['Condition2'].unique())
print("\nUnique values in 'Condition2' column in validation data:", X_valid['Condition2'].unique())

# Question 2 -
# Label Encoding

# All categorical columns
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely label encoded
good_label_cols = [col for col in object_cols if 
                   set(X_train[col]) == set(X_valid[col])]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))
        
print('Categorical columns that will be label encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)

# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

# Apply label encoder to each column with categorical data
label_encoder = LabelEncoder()
for col in good_label_cols:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_valid[col])

print("MAE from Approach 2 (Label Encoding):") 
print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))

# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
print(sorted(d.items(), key=lambda x: x[1]))


# Question 3 - 
# Investigating Cardinality
# Cardinality is the number of unique types of categorical data in a column


# Fill in the line below: How many categorical variables in the training data
# have cardinality greater than 10?
high_cardinality_numcols = 3

# Fill in the line below: How many columns are needed to one-hot encode the 
# 'Neighborhood' variable in the training data?
num_cols_neighborhood = 25

# For large datasets with many rows, one-hot encoding can greatly expand the size of the dataset.
# For this reason, we typically will only one-hot encode columns with relatively low cardinality.
# Then, high cardinality columns can either be dropped from the dataset, or we can use label encoding.

# As an example, consider a dataset with 10,000 rows, and containing one categorical column with 100 unique entries.

# Fill in the line below: How many entries are added to the dataset by 
# replacing the column with a one-hot encoding?
OH_entries_added = 990000

# Fill in the line below: How many entries are added to the dataset by
# replacing the column with a label encoding?
label_entries_added = 0

# Next, you'll experiment with one-hot encoding. But, instead of encoding all of the categorical variables in the dataset,
# you'll only create a one-hot encoding for columns with cardinality less than 10.

# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)


# Question 4 - 
# One Hot Encoding

OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

print("MAE from Approach 3 (One-Hot Encoding):") 
print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))

## Submission
imputer = SimpleImputer(strategy = 'most_frequent')
imputed_X_test = pd.DataFrame(imputer.transform(X_test[object_cols]))
imputed_X_test.columns = X_test[object_cols].columns

OH_cols_X_test = pd.DataFrame(OH_encoder.transform(imputed_X_test[low_cardinality_cols]))

OH_cols_X_test.index = imputed_X_test.index

num_X_test = imputed_X_test.drop(object_cols,axis=1)

# OH_X_test = pd.concat([num_X_test,OH_cols_X_test],axis=1)

# Model created for data submission
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(OH_X_train, y_train)
preds = model.predict(OH_X_test)

print(len(preds))

# Save test predictions to file
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds})
output.to_csv('03-submission.csv', index=False)


# X_test_cat_nan_colnames = ['MSZoning','Utilities', 'Exterior1st','Exterior2nd','KitchenQual','Functional','SaleType']
# X_test_num_nan_colnames = ['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea']
# X_test_cat_nan = X_test.loc[:, X_test_cat_nan_colnames]
# X_test_num_nan = X_test.loc[:,X_test_num_nan_colnames]

# cat_imputer = SimpleImputer(strategy='most_frequent')
# num_imputer = SimpleImputer(strategy='median')

# X_test_cat_nan_imputer = pd.DataFrame(cat_imputer.fit_transform(X_test_cat_nan))
# X_test_cat_nan_imputer.columns = X_test_cat_nan.columns
# X_test_cat_nan_imputer.index = X_test_cat_nan.index

# X_test_num_nan_imputer = pd.DataFrame(num_imputer.fit_transform(X_test_num_nan))
# X_test_num_nan_imputer.columns = X_test_num_nan.columns
# X_test_num_nan_imputer.index = X_test_num_nan.index

# X_test.drop(X_test_cat_nan_colnames, axis=1, inplace=True)
# X_test.drop(X_test_num_nan_colnames, axis=1, inplace=True)

# X_test = pd.concat([X_test,X_test_cat_nan_imputer], axis=1)
# X_test = pd.concat([X_test,X_test_num_nan_imputer], axis=1)

# print(X_test.shape)

# OH_cols_test = pd.DataFrame(OH_encoder.transform(X_test[low_cardinality_cols]))

# OH_cols_test.index = X_test.index

# num_X_test = X_test.drop(object_cols, axis=1)

# OH_X_test = pd.concat([num_X_test, OH_cols_test], axis=1)

# my_model = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)

# my_model.fit(OH_X_train, y_train)

# # Generate test predictions
# preds_test = my_model.predict(OH_X_test)

# output = pd.DataFrame({'Id': OH_X_test.index,
#                        'SalePrice': preds_test})
# output.to_csv('03-submission.csv', index=False)