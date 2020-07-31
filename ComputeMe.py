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

if number == c:
    print(number, 'is correct.')
else:
    print(number, 'is wrong.')
    print('Correct result:', c)
