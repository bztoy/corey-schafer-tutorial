from utilities import (space, separated, start, end, sub, new_topic)
import os

# Key
key = 'file_objects_readfiles'


def run():
    start('File objects: Read file')
    work_dir = os.environ.get('PYTHON_TEMP')
    file_path = os.path.join(work_dir, 'birds.txt')
    new_topic(
        'Read file with open(), !!! file must be closed after use with method close()')
    # r = read, w = write, a = append, r+
    f = open(file_path, 'r')
    print(f'filename is: {f.name}, mode is {f.mode}')
    f.close()

    new_topic('Working on file with Context Manager (with)', True)
    # file will be closed autometically
    with open(file_path, 'r') as f:
        print(f'filename is: {f.name}, mode is {f.mode}')
        new_topic('Read all file contents with method read()', True)
        f_contents = f.read()
        print(f_contents)

    with open(file_path, 'r') as f:
        new_topic(
            'Get a list of line in file contents with method readlines()', True)
        # readlines() will retern a list of lines in the file
        f_contents = f.readlines()
        print(f_contents)

    with open(file_path, 'r') as f:
        new_topic('Read single line with method readline()', True)
        # readline() will move the cursor to the next line by default
        f_contents = f.readline()
        print(f_contents)
        f_contents = f.readline()
        print(f_contents)
        f_contents = f.readline()
        print(f_contents, end='')

    new_topic(
        'Using for loop to read file, this will consume memory time by time', True)
    with open(file_path, 'r') as f:
        for line in f:
            print(line, end='')

    new_topic('Read file by read(<size>)', True)
    with open(file_path, 'r') as f:
        f_contents = f.read(10)
        print(f_contents, end='')
        f_contents = f.read(10)
        print(f_contents, end='')
        f_contents = f.read(10)
        print(f_contents, end='')

    new_topic('Read file by read(<size>) under while loop', True)
    with open(file_path, 'r') as f:
        size_to_read = 10
        f_contents = f.read(size_to_read)

        while len(f_contents) > 0:
            print(f_contents, end='*')
            f_contents = f.read(size_to_read)
        print('')

    new_topic('Using seek() method to go to any position ', True)
    with open(file_path, 'r') as f:
        size_to_read = 10
        f_contents = f.read(size_to_read)
        print(f_contents, end='')
        f.seek(0)
        f_contents = f.read(size_to_read)
        print(f_contents)

    end()
