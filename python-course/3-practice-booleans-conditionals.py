# Practice 3 - Booleans and Conditionals

### Question 1 - 

# Many programming languages have sign available as a built-in function.
# Python doesn't, but we can define our own!

# Define a function called sign which takes a numerical argument
# and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(num):
    if(num == 0):
        return(0)
    elif(num > 0):
        return(1)
    elif(num < 0):
        return(-1)


### Question 2 - 

# We've decided to add "logging" to our to_smash function from the previous exercise.
# Modify the definition in the cell below to correct the grammar of our print statement. 
# (If there's only one candy, we should use the singular "candy" instead of the plural "candies")

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if(total_candies == 1):
        print("Splitting", total_candies, "candy")    
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

    # print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

to_smash(91)
to_smash(1)


### Question 3 - 

# In the main lesson we talked about deciding whether we're prepared for the weather.
# I said that I'm safe from today's weather if...

# I have an umbrella...
# or if the rain isn't too heavy and I have a hood...
# otherwise, I'm still fine unless it's raining and it's a workday
# The function below uses our first attempt at turning this logic into a Python expression.

# I claimed that there was a bug in that code. Can you find it?


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# 1 - 5 and have_hood
# 2 - 0 and is_workday
# 3 - have_umbrella or rain_level
# 4 - 5 and have_hood or not rain_level


# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


### Question 4 - 

# The function is_negative below is implemented correctly -
# it returns True if the given number is negative and False otherwise.

# However, it's more verbose than it needs to be. 
# We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

# def concise_is_negative(number):
#     return(True if number < 0 else False)

def concise_is_negative(number):
    return number < 0

print(is_negative(1))
print(is_negative(-1))

print(concise_is_negative(1))
print(concise_is_negative(-1))


### Question 5 - 

# The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog.
# We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return (ketchup and mustard and onion)

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    # return ketchup  != mustard

### Question 6 - 

# We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise.
# What happens if we call int() on a bool? Try it out in the notebook cell below.

a = True
print(int(a))

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    # return(True if(int(ketchup) + int(mustard) + int(onion) == 1) else False)
    # return(int(ketchup) + int(mustard) + int(onion) == 1)
    return ketchup + mustard + onion == 1

print(exactly_one_sauce(True, False, False))
print(exactly_one_sauce(True, True, False))
print(exactly_one_sauce(True, True, True))


### Question 7 - 

# In this problem we'll be working with a simplified version of blackjack (aka twenty-one).
# In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

# The player is dealt two face-up cards. The dealer is dealt one face-up card.
# The player may ask to be dealt another card ('hit') as many times as they wish.
# If the sum of their cards exceeds 21, they lose the round immediately.
# The dealer then deals additional cards to himself until either:
#     the sum of the dealer's cards exceeds 21, in which case the player wins the round
#     the sum of the dealer's cards is greater than or equal to 17. 
#     If the player's total is greater than the dealer's, the player wins. 
#     Otherwise, the dealer wins (even in case of a tie).

# When calculating the sum of cards, Jack, Queen, and King count for 10.
# Aces can count as 1 or 11 (when referring to a player's "total" above,
# we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)

# For this problem, you'll write a function representing the player's decision-making strategy in this game.
# We've provided a very unintelligent implementation below:

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    if (player_total <= 11)
        return True
    else:
        return False

