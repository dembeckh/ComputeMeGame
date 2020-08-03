# Random generator
import random
random.seed()

# Define Task function
def task():
    a = random.randint(1,10)
    b = random.randint(1,10)
    result = a + b
    print('The task:', a, '+', b)
    return result

# Define Assessment function
def assessment(number, result):
    if number == c:
        print(number, 'is correct.')
    elif number < 0 or number > 100:
        print(number, 'is soooo wrong')
    elif c-1 <= number <= c+1:
        print(number, 'is very close.')
    else:
        print(number, 'is wrong.')

# task
c = task()

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
        number = int(input('Please enter your result: '))
    except:
        print('You did not enter an integer.')
        continue

    # assessment
    assessment(number, c)
# End
print('Correct result:', c)
print('Number attempts:', attempt)
