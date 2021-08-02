# 4 Lesson - Character Encoding

import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)

# start with a string
before = "This is the euro symbol: €"

# check to see what datatype it is
print(type(before))

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("utf-8", errors="replace")

# check the type
print(type(after))

print(after)

# convert it back to utf-8
print(after.decode("utf-8"))

# try to decode our bytes with the ascii encoding
# print(after.decode("ascii"))

# start with a string
before = "This is the euro symbol: €"

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("ascii", errors = "replace")

# convert it back to utf-8
print(after.decode("ascii"))

# We've lost the original underlying byte string! It's been 
# replaced with the underlying byte string for the unknown character :(

# Read data
kickstarters_2017 = pd.read_csv("../kaggle-datasets/12-kickstarter-projects/ks-projects-201801.csv")
print(kickstarters_2017.head())

# look at the first ten thousand bytes to guess the character encoding
with open("../kaggle-datasets/12-kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)

# Read data
kickstarters_2017 = pd.read_csv("../kaggle-datasets/12-kickstarter-projects/ks-projects-201801.csv", encoding='Windows-1252')
print(kickstarters_2017.head())