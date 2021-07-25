'''
LEGB.
Local, Enclosing, Global, Built-in
'''

import builtins
from utilities import (space, separated, start, end)

# Key
key = 'fundamental_scope'

# Python checks Local -> Enclosing -> Global -> Built-in

x = 'global x'
tesla = 'Model S'


def local_vars():
    x = 'local X'
    return x


def print_str(prefix, str):
    print(f'{prefix} : {str}')


def work_with_global():
    global tesla
    tesla = 'Model 3'

    print(f'tesla inside function: {tesla}')


def outer():
    x = 'outer x'
    y = 'outer y'
    z = 'outer z'

    def inner():
        x = 'inner x'

        nonlocal z
        z = 'mod by innder z'
        print(x, y, z)

    inner()
    print(x, y, z)


def run():
    start('Scope')
    print('Global and Local scope')
    print(f'global: {x}')
    print(f'local: {local_vars()}')
    separated()

    print('Works with Global')
    print(f'global testla before: {tesla}')
    work_with_global()
    print(f'global testla after: {tesla}')
    separated()

    print('Built-in, becareful built-in function name')
    m = min([5, 3, 8, 11, 7, 1, 2])
    print(m)

    print('List of Built-in functions')
    print(dir(builtins))
    separated()

    print('Enclosing (Nasted functions)')
    print('x = local, y = enclosing, z = overide enclosing')
    outer()
    print(x)

    end()
