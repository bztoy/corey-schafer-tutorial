import sys
from utilities import (space, separated, start, end)

# Import modules from another directory (not in the project path)
sys.path.append('D:\\Dev\\Python\\test_modules')
from moto import moto_info

# Key
key = 'module_stdlib_module'


def run():
    start('Modules and standard library')

    print('System Path')
    print(sys.path)
    separated()

    print('Import modules from outside project directory')
    moto_info()

    end()
