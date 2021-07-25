from utilities import (space, separated, start, end, sub, new_topic)
import os

# Key
key = 'mini_project_auto_parsing_and_rename_multi_files'


def run():
    main()


def main():
    start('Automate Parsing and Renaming of Multiple Files')
    # Set working directory
    new_topic('Set working directory')
    working_on_dir = os.path.join(os.environ.get('PYTHON_TEMP'), 'texts')
    print(working_on_dir)
    os.chdir(working_on_dir)
    new_topic('List of current files in the directory (before)', True)
    list_files(working_on_dir)

    for f in os.listdir():
        # If .DS_Store file is created, ignore it
        if f == '.DS_Store':
            continue
        # Set new file name
        new_name = set_new_name(f)
        # Rename
        os.rename(f, new_name)

    new_topic('List of current files in the directory (after)', True)
    list_files(working_on_dir)

    end()


def list_files(directory):
    for f in os.listdir(directory):
        print(f)


def set_new_name(file):
    # Split path and file
    f_name, f_ext = os.path.splitext(file)

    # Split filename at - into three contexts
    f_title, f_course, f_number = f_name.split('-')

    # Remove trailing space
    # One thing I noticed about this output is that if it was sorted by filename
    # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
    # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
    # We can do this in Python with zfill
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_number = f_number.strip()[1:].zfill(2)

    return (f'{f_number}-{f_title}{f_ext}')
