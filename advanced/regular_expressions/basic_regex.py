from utilities import (space, separated, start, end, sub, new_topic)
import re

key = 'advanced_regex_basic'

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
google.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc school of rock
'''

sentence = 'Start a sentence and then bring it to an end'

# Raw string r'xxx'
norm_str = '\tTab'  # \t will be a tab
raw_str = r'\tTab'


def find_iter(str_to_search: str, source_text: str = text_to_search):
    counter = 0

    pattern = re.compile(str_to_search)
    matches = pattern.finditer(source_text)
    for match in matches:
        counter += 1

        print(match)

    if counter == 0:
        print(f'string {str_to_search} is zero matched')


def run():
    start('Regular Expression : Basic')
    sub('re.finditer')
    new_topic('String vs Raw String')
    print(f'Normal string: {norm_str}')
    print(f'Raw string: {raw_str}')

    new_topic('Search normal string with re.finditer', True)
    find_iter(r'abc')
    separated()
    find_iter(r'cba')

    # these need to be escapted . ^ $ * + ? { } [ ] \ | ( )
    new_topic('Search special char (need to be escapep) with re.finditer', True)
    find_iter(r'\.')
    separated()
    find_iter(r'google\.com')
    separated()
    find_iter(r'\s')

    new_topic('Word Boundary and not a word Boundary with re.finditer', True)
    sub('Word Boundary')
    find_iter(r'\bHa')
    separated()
    sub('Not a Word Boundary')
    find_iter(r'\BHa')

    new_topic('Begining of a string (^) with re.finditer', True)
    find_iter(r'^Start', sentence)
    separated()
    find_iter(r'^Stop', sentence)

    new_topic('End of a string ($) with re.finditer', True)
    find_iter(r'end$', sentence)
    separated()
    find_iter(r'eat$', sentence)

    end()
