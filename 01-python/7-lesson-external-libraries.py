# Lesson 7 - External Libraries

# Math module
import math

print("It's math! It has type {}".format(type(math)))

# Print all functions of a module
print(dir(math))

# Access with .
print(math.pi)
print("{:.4}".format(math.pi))

print(math.log(32, 2))
# help(math.log)

print(math.log(math.e))

# help(math)

# Other import sintax

import math as m
print(m.pi)

from math import *
print(pi, log(32, 2))

# A good compromise is to import only the specific things we'll need from each module
from math import log, pi
print(pi, log(32, 2))

# Submodules

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Rolling dices
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# Understanding strange objects

# What is it
print(type(rolls))

# What can I do with
print(dir(rolls))

# What can I do with its data
print(rolls.mean())

# What can I do with check to list
print(rolls.tolist())

# Sum 10 to each roll
print(rolls + 10)

# Rolls <= 3
print(rolls <= 3)

xlist = [[1,2,3],[2,4,6],]

# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

print(x[1,-1])

# import tensorflow as tf

# # Create two constants, each with value 1
# a = tf.constant(1)
# b = tf.constant(1)

# # Add them together to get...
# print(a + b)

x = 3

print(x in [1, 2, 3])
print([1, 2, 3].__contains__(x))