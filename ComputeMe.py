# Importing random module
import random

# Initialising random generator
random.seed()

# Random values and calculation
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print('The task:', a, '+', b)

# for loop
for attempt in range(1,10):
        # Input
    number = int(input('Please enter your result:'))

    # Assessment
    if number == c:
        print(number, 'is correct.')
        # Cancel loop
        break
    elif number < 0 or number > 100:
        print(number, 'is soooo wrong')
    elif c-1 <= number <= c+1:
        print(number, 'is very close.')
    else:
        print(number, 'is wrong.')

# End
print('Correct result:', c)
print('Number attempts', attempt)
