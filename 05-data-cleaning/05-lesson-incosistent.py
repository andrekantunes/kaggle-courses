# 5 Lesson - Inconsistent Data Entry

import pandas as pd
import numpy as np

# helpful modules
import fuzzywuzzy
from fuzzywuzzy import process
import chardet

countries = [' Germany', ' New Zealand', ' Sweden', ' USA', 'Australia',
             'Austria', 'Canada', 'China', 'Finland', 'France', 'Greece',
             'HongKong', 'Ireland', 'Italy', 'Japan', 'Macau', 'Malaysia',
             'Mauritius', 'Netherland', 'New Zealand', 'Norway', 'Pakistan',
             'Portugal', 'Russian Federation', 'Saudi Arabia', 'Scotland',
             'Singapore', 'South Korea', 'SouthKorea', 'Spain', 'Sweden',
             'Thailand', 'Turkey', 'UK', 'USA', 'USofA', 'Urbana', 'germany']
print(countries)

# To lower and strip spaces
# countries = [x.lower().strip() for x in countries]
countries = list(map(lambda x: x.lower().strip(), countries))
print(countries)

# Keep unique values
countries = set(countries)

# get the top 10 closest matches to "south korea"
matches = fuzzywuzzy.process.extract("south korea", 
                                     countries,
                                     limit=10,
                                     scorer=fuzzywuzzy.fuzz.token_sort_ratio)
print(matches)                                     

# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")