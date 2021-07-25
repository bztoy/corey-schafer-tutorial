from utilities import (space, separated, start, end)
from operator import attrgetter

# Key
key = 'sorting_objs'

li = [9, 1, 2, 8, 7, 5, 4, 3, 6]
tup = (9, 1, 2, 8, 7, 5, 4, 3, 6)
di = {'name': 'toy', 'job': 'programmer', 'age': None, 'os': 'Windoes'}

# Notes
# Tuple does not have .sort() method
# Object could not be sorted directly, we need to privide key


class Employee():
    def __init__(self, name, age, salary):
        super().__init__()
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        # return super().__repr__()
        return f'{self.name} {self.age} ${self.salary}'


e1 = Employee('John', 25, 80000)
e2 = Employee('Cate', 24, 75000)
e3 = Employee('Zix', 26, 95000)
e4 = Employee('Matt', 28, 120000)

employee = [e1, e2, e3, e4]


def e_nsort(emp):
    '''A helper function.'''
    return emp.name


def e_ssort(emp):
    '''A helper function.'''
    return emp.salary


def run():
    start('Sorting')

    print(f'raw data: {li}')
    print(f'sorted function: {sorted(li)}')
    li.sort()
    print(f'sort() method: {li}')
    separated()
    print('Sort descending')
    sd_li = sorted(li, reverse=True)
    print(sd_li)
    separated()

    print('Sorting tuple')
    print(f'raw data: {tup}')
    # the sort funtion always return a list
    print(f'sorted function: {tuple(sorted(tup))}')
    separated()

    print('Sorting Dictionary')
    print(f'Dict data are: {di}')
    s_di = sorted(di)
    print(f'sorted funct will sort only the key {s_di}')
    separated()

    print('Sort with condition(s)')
    nli = [-6, -4, 3, 1, -7, 2, 0]
    s_nli = sorted(nli)
    print(f'default sort: {s_nli}')
    s_nli = sorted(nli, key=abs)
    print(f'sort with key:abs : {s_nli}')
    separated()

    print('Object with a helper function')
    print(employee)
    print('Sorted by name')
    s_employee = sorted(employee, key=e_nsort)
    print(s_employee)
    print('Sorted by Salary Descending')
    s_employee = sorted(employee, reverse=True, key=e_ssort)
    print(s_employee)
    separated()

    print('Object with lambda')
    print(employee)
    print('Sorted by name')
    s_employee = sorted(employee, key=lambda e: e.name)
    print(s_employee)
    print('Sorted by Salary Descending')
    s_employee = sorted(employee, reverse=True, key=lambda e: e.salary)
    print(s_employee)
    separated()

    print('Object with attrgetter')
    print(employee)
    print('Sorted by age')
    s_employee = sorted(employee, key=attrgetter('age'))
    print(s_employee)

    end()
