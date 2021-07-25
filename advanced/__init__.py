from advanced.slicing import slist, sstring
from advanced.comprehensions import list_comph, dict_comph, set_comph
from advanced.sorting import sorted_objs
from advanced.string_formats import str_formats
from advanced.regular_expressions import basic_regex

# Key
key = 'advanced'

# Switch
sw = {
    # Slicing
    slist.key: False,
    sstring.key: False,

    # Comprehension
    list_comph.key: False,
    dict_comph.key: False,
    set_comph.key: False,

    # Sorting
    sorted_objs.key: False,

    # String format
    str_formats.key: False,

    # Regular Expression
    basic_regex.key: True
}


def run():
    # Slicing List/String
    if sw[slist.key]:
        slist.run()

    if sw[sstring.key]:
        sstring.run()

    # Comprehensions (List/Dict/Set)
    if sw[list_comph.key]:
        list_comph.run()

    if sw[dict_comph.key]:
        dict_comph.run()

    if sw[set_comph.key]:
        set_comph.run()

    # Sorting
    if sw[sorted_objs.key]:
        sorted_objs.run()

    # String format
    if sw[str_formats.key]:
        str_formats.run()

    # Regular Expression
    if sw[basic_regex.key]:
        basic_regex.run()
