from utilities import (space, separated, start, end)
import math

# Key
key = 'functions_func'

# keyword pass is for an empty function


def run():
    start('Functions')

    print(f'This is an empty function')
    empty_function()
    print(empty_function())
    separated()

    print('function with simple return value')
    radius = 4
    print(
        f'the area of a circle with radius {radius} is {circle_area(radius)}')

    separated()
    print('function with default parameter value')
    print(greeting('Good morning'))
    print(greeting('Good morning', 'Ken'))

    separated()
    print('basic function with *args and **kwargs parameters')
    student_info('Math', 'Music', name='Pat', age=19, graduated=False)

    separated()
    courses = ['Math', 'Physic']
    info = {'name': 'Pat', 'age': 19, 'graduated': False}
    print('pass list and dict variables as parameter of func with *args and **kwargs (packed)')
    student_info(courses, info)

    print('pass list and dict variables as parameter of func with *args and **kwargs (Unpacked)')
    student_info(*courses, **info)
    separated()

    print('function with doc string')
    space()
    print(good_drinks('milk'))
    print(good_drinks('cola'))
    print(good_drinks('beer'))

    end()


def empty_function():
    pass


def circle_area(radius):
    return (math.pi * (radius * radius))


def greeting(greeting, you='You'):
    return (f'{greeting}, {you}')


def student_info(*args, **kwargs):
    # arges = a tuple of value = (val1, val2,..., val2)
    print(args)
    # kwarges = a dict of key-value = {key1:val1, key2:val2,...,keyn:valn}
    print(kwargs)


def good_drinks(drink):
    """Return suggestion about the drink"""

    good_lists = ['water', 'minare water', 'milk']
    okay_lists = ['black coffee', 'black tea']
    yakky_lists = ['cola', 'soda']

    if drink in good_lists:
        return(f'{drink} is definitely a good choice')
    elif drink in okay_lists:
        return(f'it is okay to drink {drink} regulary')
    elif drink in yakky_lists:
        return f'{drink}! you shoud looks to another menu'
    else:
        return f'lets me try {drink} first :p'


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
