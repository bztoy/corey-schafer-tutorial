from utilities import (space, separated, start, end)

# Key
key = 'str_options'


def run():
    start('String Options')
    message = 'Alex Rins (No.42) is a Suzuki MotoGP rider, He is a Spanish and live in Spain'
    print(f'Working on string: "{message}"')
    separated()

    # lower case
    print(f'convert to lower case: {message.lower()}')

    # upper case
    print(f'convert to upper case: {message.upper()}')

    # count method : count the specific word or char in a target string
    space()
    count_me = 'is'
    print(
        f'word counting, "{count_me}" have found {message.count(count_me)} in total')

    # Find : return the first position (if found) or return -1 if doesn't match any
    space()
    find_me = ['Moto', 'Sky']
    print(
        f'Find "{find_me[0]}" = {message.find(find_me[0])} and Find "{find_me[1]}" is {message.find(find_me[1])}')

    # Replace
    space()
    message = 'I like to drink coffee with milk'
    print(f'original string is: "{message}"')
    message = message.replace('coffee', 'tea')
    print(f'after replace coffee with tea, new string will be "{message}"')

    # Concate
    space()
    greeting = 'Good morning'
    name = 'Pat'
    message = greeting + ' ' + name + ' welcome'
    print(""""Here are string concatenate options""")
    print('1. with + sign: ', message)
    print('2. with .format: ', '{} {} welcome'.format(greeting, name))
    print(f'3. with f string: {greeting} {name} welcome')

    end()
