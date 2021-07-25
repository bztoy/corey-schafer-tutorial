from utilities import (space, separated, start, end)

# Key
key = 'loops_and_interations_loops'

# break command is used to exit the loops
# continue : skip to next iteration
# force exit loop by Ctrl + c


def run():
    start('Loops')

    nums = [1, 2, 3, 4, 5]

    print('this is for loop with break, it will be stopped when number is 3')
    for num in nums:
        print(num)
        if num == 3:
            break

    separated()

    print('this is for loop with continue, it will be skip the operation when number are 2 and 4')
    for num in nums:
        if num in [2, 4]:
            print(f'skip {num} number')
            continue
        print(num)

    separated()

    print('Nested loops')
    for num in [1, 2, 3]:
        for char in 'ABC':
            print(char + str(num))

    separated()

    print('for loop in a range, start at 5')
    for i in range(5, 11):
        print(i)

    separated()

    print('while loop with break')
    x = 0
    while x < 7:
        print(x)
        x += 1
        if x == 5:
            break

    end()
