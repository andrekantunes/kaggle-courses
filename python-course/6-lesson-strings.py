# Lesson 6 - Strings

x = 'Pluto is a planet'
y = "Pluto is a planet"

print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

# Escaping single quotes with backslash

print('Pluto\'s a planet!')

# \'
# \"
# \\
# \n	

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""

print(triplequoted_hello)
print(triplequoted_hello == hello)

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# Strings are sequences

planet = 'Pluto'
print(planet[0])

# Slicing

print(planet[-3:])

print(len(planet))

print([char+'! ' for char in planet])

claim = "Pluto is a planet!"
print(claim.upper())
print(claim.lower())
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('dwarf planet'))

# Strings and lists .split() and .join()

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

print(year)
print(month)
print(day)

print('/'.join([month, day, year]))

print(' 👏 '.join([word.upper() for word in words]))

# Building strings with format

print(planet + ', we miss you.')

position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

#         2 decimal points   3 decimal points, format as percent     separate with commas
print(
    "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
    )
)

# Format with arguments by index

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Dictionaries

# one, two, three - Keys
# 1, 2, 3 - Values
numbers = {'one':1, 'two':2, 'three':3}

print(numbers['one'])

# Change values 

numbers['one'] = 'Pluto'
print(numbers)

t = (1,2,3)
l = [1,2,3]
d = {'one':1, 'two':2, 'three':3}

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# Search for key in dictionary

print('Saturn' in planet_to_initial)
print('Betelgeuse' in planet_to_initial)

# for loop over a dictionary loop over keys

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# access values and keys .values and .keys

print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))