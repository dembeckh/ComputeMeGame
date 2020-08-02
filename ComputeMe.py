# Importing random module
import random

# Initialising random generator
random.seed()

# Random values and calculation
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print('The task:', a, '+', b)

# Initialising loop
number = c + 1

# Initialising attempts
attempt = 0

# while loop
while number != c:

    # Number attempts
    attempt += 1

    # Input with exception handling
    try:
        number = int(input('Please enter your result:'))
    except:
        print('You did not enter an integer.')
        continue

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
print('Number attempts:', attempt)
