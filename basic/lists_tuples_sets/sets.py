from utilities import (space, separated, start, end)

key = 'lts_sets'

# Set: no duplicated value, no order


def run():
    start('Sets')

    # Only 1 Apple will be shown
    fruits = {'Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Apple'}
    print(f'This is set: {fruits}')
    separated()

    # In operand
    print('Set can use "in" to check if the specified value is its member or not')
    fruit = 'Papaya'
    print(f'Is {fruit} in this set? : {fruit in fruits}')
    separated()

    print('from these 2 sets')
    thai_fruits = {'Banana', 'Durian', 'Mango', 'Pineapple', 'Orange', 'Grape'}
    chinese_fruits = {'Apple', 'Peach', 'Orange', 'Grape', 'Strawberry'}

    print(f'Thai fruits: {thai_fruits} ')
    print(f'Chinese fruits: {chinese_fruits} ')
    space()

    # Intersection
    print(f'Thai fruits intersection with Chinese fruits are')
    print(thai_fruits.intersection(chinese_fruits))

    # Difference
    print(f'Thai fruits that not found in Chinese fruits are')
    print(thai_fruits.difference(chinese_fruits))

    # Union
    print(f'Thai fruits union with Chinese fruits are')
    print(thai_fruits.union(chinese_fruits))

    end()
