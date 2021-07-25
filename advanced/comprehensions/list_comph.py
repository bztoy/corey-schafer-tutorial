from utilities import (space, separated, start, end)

# Key
key = 'comprehensions_list'

# List of numbers
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def run():
    start('List comprehensions')
    print(f'start from this list {nums}')
    print('comprehensions #1: n from n')
    nlist = [n for n in nums]
    print(f'[n for n in nums] = {nlist}')
    separated()
    print('comprehensions #2: n*n from n')
    nlist = [n * n for n in nums]
    print(f'[n*n for n in nums] = {nlist}')
    separated()
    print('comprehensions #3: a map + lambda')
    nlist = list(map(lambda n: n * n, nums))
    print(f'[map(lambda n: n*n, nums)] = {nlist}')
    separated()
    print('comprehensions #4: "n" for each "n" in nums if even ')
    nlist = [n for n in nums if n % 2 == 0]
    print(f'[n for n in nums if n%2 == 0] = {nlist}')
    separated()
    print(
        f'comprehensions #5: list(filter(lambda n: n % 2 == 0, nums)) = {nlist}')
    nlist = list(filter(lambda n: (n % 2) == 0, nums))
    print(nlist)
    separated()
    print(
        f'comprehensions #6: a (letter, num) pair for each letters in "abcd" and each number in "0123"')
    my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
    print(my_list)

    end()
