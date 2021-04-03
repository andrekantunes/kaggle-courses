spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# Types of variables and operations

a = 15
b = 7.25
c = "teste"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("True Division: ", a / b)
print("Floor Division: ", a // b)
print("Modulus: ", a % b)
print("Exponential: ", a ** b)
print("Negation: ", -a)

# Builtin functions

vector = [1, 2, 3, 4, 5]

print("Minimal value: ", min(vector))
print("Maximal value: ", max(vector))

print(abs(32))
print(abs(-32))

# Casting

print(float(10))
print(int(12.25))
print(int('807') + 1)