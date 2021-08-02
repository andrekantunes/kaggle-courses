# 4 Practice - Character Encoding

import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)

# Question 1 -
# What are encodings
sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

before = sample_entry.decode("big5-tw") 
new_entry = before.encode("utf-8", errors = "replace")

print(new_entry)