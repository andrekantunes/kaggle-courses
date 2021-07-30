# Lesson 2 - Scaling and Normalization

import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# set seed for reproducibility
np.random.seed(0)

# Scaling - changing range of the data // 0 - 100 // 0 - 1
#   Use in methods based on measures of how far apart data points are
#   SVM, KNN

# generate 1000 data points randomly drawn from an exponential distribution
original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])

# plot both together to compare
fig, ax = plt.subplots(1,2)
sns.displot(original_data, ax=ax[0])
ax[0].set_title("Original Data")
sns.displot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")

plt.show()

# Normalization - changing the shape of the distribution

