# Automated Machine Learning

### Steps on Machine Learning

# Step 1: Gather the data. 
# In industry, there are important considerations you need to take into account when building a dataset,
# such as target leakage. When participating in a Kaggle competition, this step is already completed for you.

# Step 2: Prepare the data - Deal with missing values and categorical data.
# (Feature engineering is covered in a separate course.)

# Step 3: Select a model. There are a lot of different types of models. Which one should you select for your problem?

# Step 4: Train the model - Fit decision trees and random forests to patterns in training data.

# Step 5: Evaluate the model - Use a validation set to assess how well a trained model performs on unseen data.

# Step 6: Tune parameters - Tune parameters to get better performance from XGBoost models.

# Step 7: Get predictions - Generate predictions with a trained model and submit your results to a Kaggle competition.

### Using Google Cloud AutoML Tables 

# Save CSV file with first 2 million rows only

# import pandas as pd

# train_df = pd.read_csv("train.csv", nrows = 2_000_000)
# train_df.to_csv("train_small.csv", index=False)

### Variables to use AutoML

# PROJECT_ID - The name of your Google Cloud project. All of the work that you'll do in Google Cloud is organized in "projects".

# BUCKET_NAME - The name of your Google Cloud storage bucket. In order to work with AutoML, we'll need to create a storage bucket, where we'll upload the Kaggle dataset.

# DATASET_DISPLAY_NAME - The name of your dataset.

# TRAIN_FILEPATH - The filepath for the training data (train.csv file) from the competition.

# TEST_FILEPATH - The filepath for the test data (test.csv file) from the competition.

# TARGET_COLUMN - The name of the column in your training data that contains the values you'd like to predict.

# ID_COLUMN - The name of the column containing IDs.

# MODEL_DISPLAY_NAME - The name of your model.

# TRAIN_BUDGET - How long you want your model to train (use 1000 for 1 hour, 2000 for 2 hours, and so on).

PROJECT_ID = 'kaggle-playground-170215'
BUCKET_NAME = 'automl-tutorial-alexis'

DATASET_DISPLAY_NAME = 'taxi_fare_dataset'
TRAIN_FILEPATH = "train_small.csv" 
TEST_FILEPATH = "test.csv"

TARGET_COLUMN = 'fare_amount'
ID_COLUMN = 'key'

MODEL_DISPLAY_NAME = 'tutorial_model'
TRAIN_BUDGET = 4000

# Import the class defining the wrapper
from google.cloud import AutoMLTablesWrapper

# Create an instance of the wrapper
amw = AutoMLTablesWrapper(project_id=PROJECT_ID,
                          bucket_name=BUCKET_NAME,
                          dataset_display_name=DATASET_DISPLAY_NAME,
                          train_filepath=TRAIN_FILEPATH,
                          test_filepath=TEST_FILEPATH,
                          target_column=TARGET_COLUMN,
                          id_column=ID_COLUMN,
                          model_display_name=MODEL_DISPLAY_NAME,
                          train_budget=TRAIN_BUDGET)

# Create and train the model
amw.train_model()

# Get predictions
amw.get_predictions()

submission_df = pd.read_csv("../working/submission.csv")
submission_df.head()