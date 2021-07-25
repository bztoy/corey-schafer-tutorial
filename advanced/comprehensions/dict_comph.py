from utilities import (space, separated, start, end)

# Key
key = 'comprehensions_dict'

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']


def run():
    start('Dict comprehensions')
    print('Sample mappig with zip function')
    lzip = list(zip(names, heros))
    print(lzip)
    separated()

    # a dict{'name': 'hero'} for each name, hero in zip(names, heros)
    print('a dict of name:hero by dict comprehension')
    myheros = {name: hero for name, hero in zip(names, heros)}
    print(myheros)

    # with condition
    print('a dict of name:hero by dict comprehension with conditions')
    myheros = {name: hero for name, hero in zip(
        names, heros) if name not in ['Peter', 'Logan']}
    print(myheros)

    end()
