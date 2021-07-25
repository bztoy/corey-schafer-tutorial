from basic.strings import (
    string_values,
    string_length,
    string_options,
    string_extras
)
from basic.integers_and_floats import (
    arith_operators,
    arith_comparisions,
    arith_type_casting
)

from basic.lists_tuples_sets import (
    lists,
    tuples,
    sets,
    lists_tuples_sets
)

from basic.dictionaries import (
    dicts_functions
)

from basic.conditionals_booleans import (
    if_else
)

from basic.loops_and_iterations import (
    loops
)

from basic.functions import (
    functions
)

from basic.modules_and_std_lib import modules, standard_library
from basic.fundamental import scope


# Key
key = 'basic'

# Switch
sw = {
    # Strings
    string_values.key: False,
    string_length.key: False,
    string_options.key: False,
    string_extras.key: False,

    # Intergers and Floats
    arith_operators.key: False,
    arith_comparisions.key: False,
    arith_type_casting.key: False,

    # Lists, Tuples, Sets
    lists.key: False,
    tuples.key: False,
    sets.key: False,
    lists_tuples_sets.key: False,

    # Dictionaries
    dicts_functions.key: False,

    # Conditionals and Booleans
    if_else.key: False,

    # Loops and Interations
    loops.key: False,

    # Functions
    functions.key: False,

    # Modules and Standard Library
    modules.key: False,
    standard_library.key: False,

    # Fundamental
    scope.key: True
}


def run():
    # String pattern
    if sw[string_values.key]:
        string_values.run()

    # String length
    if sw[string_length.key]:
        string_length.run()

    # String options
    if sw[string_options.key]:
        string_options.run()

    # String extra functions
    if sw[string_extras.key]:
        string_extras.run()

    # Arithmethic Operators
    if sw[arith_operators.key]:
        arith_operators.run()

    # Arithmethic Camparisions
    if sw[arith_comparisions.key]:
        arith_comparisions.run()

    # Arithmethic Type Casting
    if sw[arith_type_casting.key]:
        arith_type_casting.run()

    # Lists
    if sw[lists.key]:
        lists.run()

    # Tuples
    if sw[tuples.key]:
        tuples.run()

    # Sets
    if sw[sets.key]:
        sets.run()

    # Empty List, Tuple, Set
    if sw[lists_tuples_sets.key]:
        lists_tuples_sets.run()

    # Dicationaries (Functions)
    if sw[dicts_functions.key]:
        dicts_functions.run()

    # Conditional & Boolean - If, Else
    if sw[if_else.key]:
        if_else.run()

    # Loops and Interations
    if sw[loops.key]:
        loops.run()

    # Functions
    if sw[functions.key]:
        functions.run()

    # Modules and Standard Library
    if sw[modules.key]:
        modules.run()

    if sw[standard_library.key]:
        standard_library.run()

    # Fundametal
    if sw[scope.key]:
        scope.run()
