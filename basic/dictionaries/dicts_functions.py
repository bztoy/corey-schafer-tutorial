from utilities import (space, separated, start, end)

key = 'dicts_functions'

# Dict is a Key-Value


def run():
    start('Dictionaries')

    # Empty dicts can be created by
    cats = {}
    print(f'this is an empty dict {cats}')

    # Assign value
    cats = {
        'catagory': 'land animail',
        'size': 'small',
        'legs': 4,
        'pet': True,
        'food': ['rat', 'bird', 'fish']
    }
    print(f'dict key-value will be like this')
    print(cats)
    separated()

    key_name = 'food'
    print(f'Access value by key {key_name} is {cats[key_name]}')

    # Get method
    key_name = 'size'
    result = {cats.get(key_name)}
    print(
        f'get key "{key_name}" in this dict is: {result}, the value is {cats.get(key_name)}')
    key_name = 'color'
    result = {cats.get(key_name)}
    print(
        f'get key "{key_name}" in this dict is: {result}, the value is {cats.get(key_name)}')

    # Get with assign default value
    key_name = 'sound'
    print(f'the value of key {key_name} is {cats.get(key_name, "meowwww")}')
    separated()

    # Update/Add new value
    print('this is how to add/update value of a dict')
    print('by specify key')
    cats['color'] = ['black', 'white', 'brown', 'gray']
    new_foods = cats['food'].extend(['bamboo', 'rice'])
    print('by update() method')
    cats.update({'food': new_foods, 'skill': ['run', 'walk', 'jump']})
    print(f'new value of the dict are {cats} ')
    separated()

    # Delete member
    del cats['color']
    print(f'Delete by del() function')
    print(cats)
    # Delete by method pop()
    print(f'Delete by pop() method')
    cats.pop('food')
    print(cats)

    separated()
    # Length of dict
    print(f'Length of this dict is {len(cats)}')
    # Dict items
    print(f'items() method with return attr of dict in a list of key-value')
    print(cats.items())
    separated()

    # Loop through dict with key
    print('Loop through dict with key(only)')
    for key in cats:
        print(key)

    separated()

    # Loop through dict with key and value
    print('Loop through dict with key and value')
    for key, value in cats.items():
        print(key, ':', value)

    end()
