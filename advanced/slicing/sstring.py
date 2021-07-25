from utilities import (space, separated, start, end)

# Key
key = 'advanced_slicing_string'

sample_url = 'https://blogs.sap.com'


def run():
    start('Slicing strings')
    print('Reverse the string')
    print(f'> {sample_url}')
    print(f'> {sample_url[::-1]}')
    print('get to top domain name')
    print(sample_url[-4:])

    end()
