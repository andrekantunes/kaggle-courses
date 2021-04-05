# Practice 5 - Loops and Lists

### Question 1 -

# Have you ever felt debugging involved a bit of luck?
# The following program has a bug. Try to identify the bug and fix it.

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if (num > 0) and (num % 7 == 0):
        # if (num % 7 == 0):
            return True
    return False

print(has_lucky_number([3, 14]))

# Alternative solution - any returns true if any x in iterable is true

def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

### Question 2

# a - Look at the Python expression below. What do you think we'll get when we run it?

# print([1, 2, 3, 4] > 2) - Comparison beetwen list and int not supported

# b - Implement a function that reproduces this behaviour,
# returning a list of booleans corresponding to whether the corresponding element is greater than n.

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    for element in L:
        if (element > thresh):
            L[L.index(element)] = True
        else:
            L[L.index(element)] = False
    return L

# Alternative solution 1

def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

# Alternative solution 2

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]


### Question 3 

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    i = 0
    while i < len(meals) - 1:
        if(meals[i] == meals[i + 1]):
            return True
        else:
            i += 1
    return False

# Alternative solution 1

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

### Question 4

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    total = []
    results = []
    for i in range(n_runs):
        results.append(play_slot_machine())

    for element in results:
        total += element
    
    return (total / len(results))

