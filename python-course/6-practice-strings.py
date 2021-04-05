# Practice 6 - Strings and Dictionaries

# Question 1 - 

# Let's see if you can write a function to help clean US zip code data.
# Given a string, it should return whether or not that string
# represents a valid zip code.

# For our purposes, a valid zip code is any string consisting
# of exactly 5 digits.

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return( zip_code.isdigit() and len(zip_code) == 5 )


# Question 2 -

# Your function should meet the following criteria:

# Do not include documents where the keyword string shows up only
# as a part of a larger word. 

# For example, if she were looking for the keyword “closed”,
# you would not include the string “enclosed.”

# She does not want you to distinguish upper case
# from lower case letters. 
# So the phrase “Closed the case.” would be included when the keyword
# is “closed”

# Do not let periods or commas affect what is matched.
# “It is closed.” would be included when the keyword is “closed”.
# But you can assume there are no other types of punctuation.

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville", "The cat"]

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices
        
print(word_search(doc_list, 'the'))


# Question 3 - 


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices

keyword = 'learn'


# print(enumerate(doc_list))
# indices = []
# for i, doc in enumerate(doc_list):
#    words = doc.split()
#    normalized = [word.rstrip('.,').lower() for word in words]
#    if keyword.lower() in normalized:
#        indices.append(i)
