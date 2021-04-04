# Practice 2 - Functions and Getting Help

### Question 1 - Complete the body acording to its docstring

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return(round(num, 2))

print(round_to_two_places(3.14159))


### Question 2 - The help for round says that ndigits (the second argument) may be negative. 

# What do you think will happen when it is? -> Round -1 to 10, -2 to 100, -3 to 1000
# Try some examples in the following cell?

result = round(501.884, -3)

print(result)


### Question 3 - 

# In a previous programming problem, 
# the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. 
# For the sake of their friendship, any candies left over would be smashed. 
# For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Below is a simple function that will calculate the number of candies to smash
# for any number of total candies.

# Modify it so that it optionally takes a second argument representing
# the number of friends the candies are being split between.
# If no second argument is provided, it should assume 3 friends, as before.

# Update the docstring to reflect this new behaviour.

def to_smash(total_candies, number_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between the number of friends.
        If the number of friends is not provided, 3 will be assumed

    >>> to_smash(30, 4)
    2
    """
    return total_candies % number_friends

### Question 4 - 

# It may not be fun, but reading and understanding error messages will be
# an important part of your Python career.

# Each code cell below contains some commented-out buggy code. For each cell...

# Read the code and predict what you think will happen when it's run.
# Then uncomment the code and run it to see what happens.
# (Tip: In the kernel editor, you can highlight several lines and press ctrl+/ to toggle commenting.)

# Fix the code (so that it accomplishes its intended purpose without throwing an exception)

### Question 4.a

round_to_two_places(9.9999)

### Question 4.b

x = -10
y = 5

# # Which of the two variables above has the smallest absolute value?

smallest_abs = min(abs(x), abs(y))

print(smallest_abs)

### Question 4.c - Indentation

def f(x):
    y = abs(x)
    return y

print(f(5))