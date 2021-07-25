from utilities import (space, separated, start, end)

key = 'lts_list_tuple_set'


def run():
    start('Empty List, Tuple, Set')

    print('Empty list can be created with [] and list()')
    empty_list_a = []
    empty_list_b = list()
    print(f'Here are empty lists {empty_list_a}, {empty_list_b} ')
    separated()
    print('Empty tuple can be created with () and tuple()')
    empty_tuple_a = ()
    empty_tuple_b = tuple()
    print(f'Here are empty tuples {empty_tuple_a}, {empty_tuple_b} ')
    separated()
    print('Empty set can be created with set()')
    empty_set = set()
    print(f'Here is empty set {empty_set} ')

    end()
