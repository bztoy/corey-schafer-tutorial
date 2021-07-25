from utilities import (space, separated, start, end)
import random
import math
import datetime
import calendar
import os

# Key
key = 'module_stdlib_module'


def run():
    start('Standard Library')

    print('Sample from random package')
    courses = ['Math', 'Art', 'Music', 'Physic', 'English', 'Sport']
    print(random.choice(courses))
    separated()

    print('Sample from math package')
    rads = math.radians(90)
    print(f'90 radian is {rads}')
    print(f'Sin of 90 radian is {math.sin(rads)}')
    separated()

    print('Sample from datetime package')
    today = datetime.date.today()
    print(f'Today is {today}')
    separated()

    print('Sample from calandar package')
    year = 2019
    print(f'Is {year} is leap? : {calendar.isleap(year)}')
    year = 2020
    print(f'Is {year} is leap? : {calendar.isleap(year)}')
    separated()

    print('Sample from os package')
    print(f'Current working directory is {os.getcwd()}')
    separated()

    print('Bundle file variable : where the source code stored')
    print(os.__file__)

    end()
