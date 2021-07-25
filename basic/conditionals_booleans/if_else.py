from utilities import (space, separated, start, end)

# Key
key = 'cond_boolean_if_else'

# Comparisions
# [==, !=, >, <, >=, <=, is]
# is = Object Identify

# [and, or, not]

# Python does not have switch command

# False value:
# [False, None, Zero of any numeric type, Any empty sequence(string, tuple, list), Any empty mapping(dict)]


def run():
    start('If, Elseif, Else')

    language = 'Python'
    print(f'Can you dev {language}')
    programming_language(language, None)
    separated()
    framework = 'Flask'
    print(f'Can you dev {framework} in {language}')
    programming_language(language, framework)
    separated()
    language = 'ABAP'
    print(f'Can you do {language}')
    programming_language(language, None)
    separated()
    language = 'Javascript'
    print(f'What about {language}?')
    programming_language(language, None)
    separated()
    language = 'Java'
    print(f'And if it {language}?')
    programming_language(language, None)
    separated()
    language = 'Rust'
    print(f'Our next project will use {language}?')
    programming_language(language, None)
    separated()

    # is vs ==
    print('This is the different between  "is" and "==" ')
    l1 = ['a', 'b']
    l2 = ['a', 'b']
    l3 = l1
    print('There are 3 lists (l1, l2 and l3) with the same value')
    print(f'l1: {l1}, l2: {l2}, l3: {l3}')
    print(f'Is l1 == l2 : {l1 == l2}? Is l1 is l2 : {l1 is l2}')
    print(f'Is l1 == l3 : {l1 == l3}? Is l1 is l3 : {l1 is l3}')
    separated()

    print('id() function can tell us the ID in memory of an object in python')
    print(f'ID of l1 = {id(l1)}')
    print(f'ID of l2 = {id(l2)}')
    print(f'ID of l3 = {id(l3)}')
    separated()

    # False value in Python
    print('False value in Python')
    space()
    is_this_false(False)
    is_this_false(None)
    is_this_false(0)
    is_this_false([])
    is_this_false('')
    is_this_false(())
    is_this_false('I like to eat Mango')

    end()


def programming_language(lang, framework):
    if lang == 'Python' and framework == 'Flask':
        print('Well, I can do that')
    elif lang == 'Python' and framework != 'Flask':
        if framework == None:
            print('it should be a good one')
        else:
            print('I think I can try that')
    elif lang == 'ABAP':
        print('No problem at all')
    elif lang == 'Javascript':
        print('It is going to be fun')
    elif lang == 'Java':
        print('Ohh, Java but it not bad')
    else:
        print(f'Opps, I have to learn {lang} now')


def is_this_false(condition):
    if condition:
        print(f'{condition} is evaluated to True')
    else:
        print(f'{condition} is evaluated to False')
