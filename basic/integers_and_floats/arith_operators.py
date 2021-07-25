from utilities import (space, separated, start, end)

key = 'int_flo_operators'


def run():
    mathh = {
        'n': 12,
        'f': 3.14
    }

    start('Arithmethic Operators')

    print(f'data type of {mathh["n"]} is {type(mathh["n"])}')
    print(f'data type of {mathh["f"]} is {type(mathh["f"])}')
    separated()

    # Arithmetic Operators:
    print(f'Addition:       3 + 2 = {3 + 2}')
    print(f'Subtraction:    3 - 2 = {3 - 2}')
    print(f'Multiplication: 3 * 2 = {3 * 2}')
    print(f'Division:       3 / 2 = {3 / 2}')
    print(f'Floor Division: 3 // 2 = {3 // 2}')
    print(f'Exponent:       3 ** 2 = {3 ** 2}')
    print(f'Modulus:        3 % 2 = {3 % 2}')
    separated()

    # Additional methods
    base, operand = 10, 7
    print(f'Add {operand} to {base}')
    base += operand
    print(f'result = {base}')
    base, operand = 10, 7
    print(f'Subtract {operand} from {base}')
    base -= operand
    print(f'result = {base}')
    separated()

    # ABS
    abs_value = -99
    print(f'Absolute value of {abs_value} is {abs(abs_value)}')
    # Round
    round_value = 11.468
    print(f'Rounding value of {round_value} is {round(round_value)}')
    print(
        f'Rounding value of {round_value} (2 digits) is {round(round_value, 2)}')

    end()
