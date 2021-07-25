from utilities import (space, separated, start, end)

key = 'lts_tuples'

# Tuple is immutable (unchangables)


def run():
    start('Tuples')

    fruits = ('Apple', 'Banana', 'Orange', 'Mango', 'Grape')
    print(f'This is tuple: {fruits}')
    separated()

    # for loop in tuples
    print('For loop in tuple')
    for fruit in fruits:
        print(fruit)

    # Access by index
    separated()
    print(f'Item 3 of this tuple is {fruits[3]}')

    # Access by name
    separated()
    fruit = 'Banana'
    print(f'{fruit} stored at index {fruits.index(fruit)} in the tuple')

    end()
