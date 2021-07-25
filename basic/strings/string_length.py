from utilities import (space, separated, start, end)

# Key
key = 'str_len'


def run():
    start('String Length')
    message = 'ring of the Saturn'
    print(f'We are working with string: "{message}"')

    # string length
    print(f'Total length of it is {len(message)} chars')

    separated()
    # single index
    print(f'charactors at index 5 and 9 are [{message[5]}, {message[9]}]')

    # substring (range)
    print(f'a substring from index 3 to 8 is "{message[3:8]}"')

    # substring 0-4
    print(f'a substring from the 1st - 4th is"{message[:4]}"')

    # substring 10-last
    print(f'a substring from the 10th - the last digit is "{message[10:]}"')
