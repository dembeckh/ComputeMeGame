# Random generator
import random
random.seed()

# Number of tasks
number_tasks = -1
while number_tasks < 0 or number_tasks > 10:
    try:
        number_tasks = int(input('How many tasks (1 to 10)? '))
    except:
        continue

# Number of correct results
correct_results = 0

# Loop with "number_tasks" tasks
for task in range(1, number_tasks+1):

    # Selection operator
    opnumber = random.randint(1,4)

    # Selection operand
    if(opnumber == 1):
        a = random.randint(0,30)
        b = random.randint(0,30)
        op = '+'
        c = a + b
    elif(opnumber == 2):
        a = random.randint(0,30)
        b = random.randint(0,30)
        op = '-'
        c = a - b
    elif(opnumber == 3):
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = '*'
        c = a * b
    # Special case division
    elif(opnumber == 4):
        c = random.randint(1,10)
        b = random.randint(1,10)
        op = '/'
        a = c * b

    # Task
    print(f"Task {task} of {number_tasks}: {a} {op} {b}")
    # Loop with 3 attempts
    for attempt in range(1,4):

        # Input
        try:
            number = int(input('Please enter a result: '))
        except:
            # if conversion is not successful
            print('You did not enter an integer.')
            continue

        # Assessment
        if number == c:
            print(number, 'is correct.')
            correct_results += 1
            break
        elif number < 0 or number > 100:
            print(number, 'is soooo wrong')
        elif c-1 <= number <= c+1:
            print(number, 'is very close.')
        else:
            print(number, 'is wrong.')

    # End
    print('Correct result:', c)

# Number of correct results
print(f"Total number of correct answers: {correct_results} of {number_tasks}")
