from utilities import (space, separated, start, end)
import copy

key = 'lts_lists'

# List is mutable (changeable, reference type)


def run():
    start('Lists')

    courses = ['History', 'Math', 'Physics', 'CompSci', 'English']
    print(f'List contents are {courses}')
    separated()
    print(f'Length of the list is {len(courses)}')
    print(f'Access list member at index 1 = {courses[1]}')
    # start at 1st arg but not include the 2nd agrg
    print(f'Access list members from idx 1:2 = {courses[1:3]}')
    separated()

    # Append item to the list
    new_course = 'Art'
    courses.append(new_course)
    print(f'Append {new_course} to the list and the new value are')
    print(courses)

    # Insert item (index must be specified)
    new_course = 'Cooking'
    courses.insert(1, new_course)
    print(
        f'Insert {new_course} to the 1st index of the list and its new value are')
    print(courses)

    # Extend
    new_courses = ['Health', 'Handwriting', 'Music', 'Dramatics']
    courses.extend(new_courses)
    print(
        f'Extend {new_course} to the list and its new value are')
    print(courses)
    separated()

    # Remove item with remove method
    remove_course = 'Cooking'
    courses.remove(remove_course)
    print(f'Remove {remove_course} from the list and its new value are')
    print(courses)

    # Remove the last item with pop method
    popped = courses.pop()
    print(
        f'Remove last item ({popped}) with method pop() from the list and its new value are')
    print(courses)
    separated()

    # Reverse the sequence of the list
    courses.reverse()
    print(f'The list after reversed its position are')
    print(courses)

    # Sorting
    courses.sort()
    print(f'The list after sorted are')
    print(courses)
    # Sorting (Descending)
    courses.sort(reverse=True)
    print(f'The list after sorted (Descending) are')
    print(courses)
    separated()

    # Sorting with function sorted()
    # this function will return a copy for sorted value
    courses = sorted(courses)
    print(f'Sorting the list with sorted function {courses}')

    num_list = [1, 5, 20, 98, 43, 7, 18, 30]
    print(f'from this list {num_list}')
    # Min function
    print(f'Minimum number is {min(num_list)}')
    # Max function
    print(f'Maximum number is {max(num_list)}')
    # Sum function
    print(f'Summary of this list is {sum(num_list)}')
    separated()

    print('Indexing, let swithced back to the courses list')
    print(courses)

    # Find index of a list member with method index()
    course = 'Art'
    print(
        f'This is how to find index of "{course}" in the list is {courses.index(course)}')

    # Find list member with in command (this will return True/False)
    course = 'Math'
    print(f'is "{course}" is in the list? : {course in courses}')

    course = 'Vocabulary'
    print(f'is "{course}" is in the list? : {course in courses}')
    separated()

    # For loop in the list
    print(f'For loop in the list')
    for course in courses:
        print(course)
    separated()

    # For loop in the list with enumerate function
    print(f'For loop in the list with enumerate function')
    for index, course in enumerate(courses):
        print(f'Index {index} is {course} ')

    separated()

    # For loop in the list with enumerate function (start agrg)
    print(f'For loop in the list with enumerate function from item 6')
    for index, course in enumerate(courses, start=1):
        print(f'Index {index} is {course} ')

    separated()

    # Convert list to string with join() method
    sep = ' - '
    courses_str = sep.join(courses)
    print(f'Convert list to string with .join() method')
    print(courses_str)

    # Convert string with a separator to list with .split() method
    print(f'Convert string with a separator to list with .split() method')
    new_courses = courses_str.split(sep)
    print(new_courses)

    separated()
    # List in mutable and reference type
    riders = ['MM93', 'AM73', 'AR42', 'JM36', 'AD04']
    riders_new = riders
    print(f'List is reference type')
    print(f'Riders    : {riders}')
    print(f'Riders new: {riders_new}')
    print(f'Remove the last item from Rider new then print out them again')
    riders_new.pop()
    print(f'Riders    : {riders}')
    print(f'Riders new: {riders_new}')
    separated()

    # How to actually copy/clone list
    print('There are several ways to actually copy/clone list')

    print(f'1. using .copy() method')
    riders_c1 = riders.copy()
    riders_c1.pop()
    print(f'Riders   : {riders}')
    print(f'Riders C1: {riders_c1}')
    separated()

    print(f'2. using slice')
    riders_c2 = riders[:]
    riders_c2.pop()
    print(f'Riders   : {riders}')
    print(f'Riders C3: {riders_c2}')
    separated()

    print(f'3. using list function')
    riders_c3 = list(riders)
    riders_c3.pop()
    print(f'Riders   : {riders}')
    print(f'Riders C3: {riders_c3}')
    separated()

    print(f'4. using copy() method from package copy')
    riders_c4 = copy.copy(riders)
    riders_c4.pop()
    print(f'Riders   : {riders}')
    print(f'Riders C4: {riders_c4}')
    separated()

    end()
