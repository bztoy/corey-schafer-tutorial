from utilities import (space, separated, start, end)

key = 'int_flo_type_casting'


def run():
    start('Arithmethic Type Casting')

# Type casting
    str_n1, str_n2 = '22', '33'
    str_f1, str_f2 = '44.44', '55.55'

    print(
        f'Int casting: "{str_n1}" + "{str_n1}" = {int(str_n1) + int(str_n2)} ')
    print(
        f'Float casting: "{str_f1}" + "{str_f2}" = {float(str_f1) + float(str_f2)} ')
    end()
