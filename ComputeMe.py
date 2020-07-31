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

# Assessment
if number == c:
    print(number, 'is correct.')
elif number < 0 or number > 100:
    print(number, 'is soooo wrong')
elif c-1 <= number <= c+1:
    print(number, 'is very close.')
else:
    print(number, 'is wrong.')

# End
print('Correct result:', c)
