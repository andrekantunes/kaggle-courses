# Complete the code below. In case it's helpful, here is the table of available arithmetic operations:

# a + b	Addition	Sum of a and b
# a - b	Subtraction	Difference of a and b
# a * b	Multiplication	Product of a and b
# a / b	True division	Quotient of a and b
# a // b	Floor division	Quotient of a and b, removing fractional parts
# a % b	Modulus	Integer remainder after division of a by b
# a ** b	Exponentiation	a raised to the power of b
# -a	Negation	The negative of a

### Question 1 - Circle Area

pi = 3.14159
diameter = 3

radius = diameter / 2
area = pi * radius ** 2
print("The Area of the circle is equal to: ", area,"cm")

### Question 2 - Swap variables

a = [1, 2, 3]
b = [3, 2, 1]

# Swap with temporarily variable

tmp = a
a = b
b = tmp

# Swap in online

a, b = b, a

print("Vector a: ", a)
print("Vector b: ", b)

### Question 3.a - Equation to evaluate 1 --- ( 5 - 3 // 2 )

result = (5 - 3) // 2
print("Equation result is: ", result)

### Question 3.b - Equation to evaluate 0 --- ( 8 - 3 * 2 - 1 + 1 )

result = 8 - ( 3 * 2 ) - ( 1 + 1 )
print("Equation result is: ", result)

### Question 4 

# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. 
# For the sake of their friendship, any candies left over will be smashed. 
# For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

alice_candies = 121
bob_candies = 77
carol_candies = 109

sum_candies = (alice_candies + bob_candies + carol_candies)

candies_for_each = sum_candies // 3

to_smash = sum_candies - candies_for_each * 3

print("The total number of candies is: ", sum_candies)
print("Each one will receive: ", candies_for_each, "candies")
print(to_smash, "candies will be smashed")
