from utilities import (space, separated, start, end)

# Key
key = 'str_extras'


def run():
    message = 'mango'

    start('String Extras')
    print('dir function')
    print(dir(message))
    separated()
    print('Help...')
    print(help(str.lower))
    print(help(str.find))
    end()
