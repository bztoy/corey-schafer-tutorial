from utilities import (space, separated, start, end)

# Key
key = 'slicing_list'

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  index   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# -index -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# slicing list pattern
# list[start:end:step]


def run():
    start('List Slicing')
    print(f'from 1 to the end: {my_list[1:]}')
    print(f'from -9 to -4: {my_list[-9:-4]}')
    print(f'from 2 to 8 step 2: {my_list[2:8:2]}')
    print(f'from 2 to -2: {my_list[2:-2]}')
    print(f'from -1 to 2: step -1 {my_list[-1:2:-1]}')
    print(f'from the end to the begining: step -2 {my_list[-1::-2]}')

    end()
