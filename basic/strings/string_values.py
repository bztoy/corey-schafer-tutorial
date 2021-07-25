from utilities import (space, separated, start, end)

# Key
key = 'str_values'


def run():
    start('String Vaues')
    message = ''
    # Message with single qoute
    message = "I'm a robot"
    print(f'msg with single qoute: {message}')

    # Message with double qoute
    message = '"Eearth" is our planet'
    print(f'msg with double qoute: {message}')

    # Multiline string
    message = """Line 1
    Line2
Line3
    """
    print(f'msg with multilines: {message}')

    end()
