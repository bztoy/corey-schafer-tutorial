from utilities import (space, separated, start, end)

# Key
key = 'comprehensions_set'

# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
nums_ex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


def run():
    start('Set comprehensions')
    print('Set comprehensions# 1')
    my_set = {n for n in nums}
    print(my_set)
    separated()

# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
    print('Generator Expressions')
    print('Method#1 : function -> yield')
    my_gen = gen_func(nums_ex)
    for i in my_gen:
        print(i)

    separated()
    print('Method#2 : comprehension')
    my_gen = (n * n for n in nums_ex)
    for i in my_gen:
        print(i)

    end()
