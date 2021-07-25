from utilities import (space, separated, start, end)
import datetime

# Key
key = 'stringformat_format'


person = {'name': 'Jenn', 'age': 23}


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')


def run():
    start('String format')
    sentence = 'My name is ' + person['name'] + \
        ' and I am ' + str(person['age']) + ' years old.'
    print(sentence)

    sentence = 'My name is {} and I am {} years old.'.format(
        person['name'], person['age'])
    print(sentence)

    sentence = 'My name is {0} and I am {1} years old.'.format(
        person['name'], person['age'])
    print(sentence)
    separated()

    print('f string (string fucntion)')
    print(f'My name is {person["name"]} and I am {person["age"]} years old.')
    separated()

    tag = 'h1'
    text = 'This is a headline'
    print('Useful of string format ref position')
    sentence = '<{0}>{1}</{0}>'.format(tag, text)
    print(sentence)
    separated()

    print('format with attributes of an object')
    sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
    print(sentence)
    sentence = 'My name is {name} and I am {age} years old.'.format(
        name='Jenn', age='30')
    print(sentence)
    sentence = 'My name is {name} and I am {age} years old.'.format(**person)
    print(sentence)
    separated()

    print('Format numeric')
    for i in range(1, 11):
        sentence = 'The value is {:02}'.format(i)
        print(sentence)

    separated()
    print('Format decimal')
    pi = 3.14159265
    sentence = 'Pi is equal to {:.3f}'.format(pi)
    print(sentence)

    separated()
    print('More readable large number')
    sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
    print(sentence)
    sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
    print(sentence)
    separated()

    print('Date format')
    my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
    print(f'raw date/time format: {my_date}')
    separated()

    print('Expectd format: September 24, 2016')
    sentence = '{:%B %d, %Y}'.format(my_date)
    print(sentence)
    separated()

    print('Expectd format: March 01, 2016 fell on a Tuesday and was the 061 day of the year')
    sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
        my_date)
    print(sentence)

    end()
