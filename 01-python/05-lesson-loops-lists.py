# Lesson 5 - Loops and Lists

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# for in lists

for planet in planets:
    print(planet, end=' ') # print all on same line

print()
# for in tuples

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1

for mult in multiplicands:
    product = product * mult

print(product)

# for in strings

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''

# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')    

# Range

for i in range(5):
    print("Doing important work. i =", i)

# While Loops

i = 0

while i < 10:
    print(i, end=' ')
    i += 1

print()
# List comprehensions

squares = [n**2 for n in range(10)]

# squares = []

# for n in range(10):
#     squares.append(n**2)

print(squares)

# List comprehension with if - Similar to Where in SQL

short_planets = [planet for planet in planets if len(planet) < 6]

print(short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]

# [
#     planet.upper() + '!' -> Select
#     for planet in planets  -> From
#     if len(planet) < 6      -> Where
# ]

print(loud_short_planets)

print([32 for planet in planets])

# List comprehension with min, max e sum

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# One line function that does the same thing

def count_negatives(nums):
    return len([num for num in nums if num < 0])

# Another possibility

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])