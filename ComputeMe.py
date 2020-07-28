# Importing random module
import random

# Initialising random generator
random.seed()

# Random values and calculation
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print('The task:', a, '+', b)

# Input
print('Please enter your result:')
z = input()

# Convert input to input
number = int(z)

# Output
print('Your result:', z)
print('The correct result:', c)
