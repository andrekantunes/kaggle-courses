# Lesson 4 - Lists

# Lists with [ ]

primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# List of lists

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

# List of different elements

my_favourite_things = [32, 'raindrops on roses', help]

print(planets)
print(planets[0])

# Last element

print(planets[-1])
print(planets[-2])

# Slicing lists

slice_planets = planets[0:3]
print(slice_planets)

slice_planets = planets[:3]
print(slice_planets)

slice_planets = planets[3:]
print(slice_planets)

slice_planets = planets[1:-1]
print(slice_planets)

slice_planets = planets[-3:]
print(slice_planets)

# Changing lists

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)

# List functions - length e sort

print(len(planets))

print(sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))

print(max(primes))

# Objects

### Imaginary parts of numbers

x = 12
# x is a real number, so its imaginary part is 0.

print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:

c = 12 + 3j
print(c.imag)

### Method - function attached to an object

print(x.bit_length())

# help(x.bit_length)

# List methods

# append adds to the end

planets.append('Pluto')
print(planets)

# help(planets.append)

# pop removes from the end

planets.pop()
print(planets)

# Searching lists

print(planets.index('Earth'))
# print(planets.index('Pluto'))

print("Earth" in planets)
print("Calbegraques" in planets)

# help(planets)

# Tuples with ( ) - Imutable

t = (1, 2, 3)
print(t)

# t[0] = 100

x = 0.125
print(x.as_integer_ratio())

# Swapping variables

a = 1
b = 0
a, b = b, a
print(a, b)