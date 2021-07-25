from utilities import (space, separated, start, end, sub, new_topic)
import os
from datetime import datetime


# Key
key = 'modules_os_environment_and_path'


def run():
    start('OS Module: Environment and Path')
    new_topic('Get environment with os.environ.get()')
    print(f'System parameter OS is at {os.environ.get("OS")}')
    new_topic('Join path with os.path.join()', True)
    file_path = os.path.join(os.environ.get('PYTHON_TEMP'), 'test.txt')
    print(file_path)
    new_topic('Get file name with os.path.basename()', True)
    print(os.path.basename(file_path))
    new_topic('Get path name with os.path.dirname()', True)
    print(os.path.dirname(file_path))
    new_topic('Split path name with os.path.split()', True)
    print(os.path.split(file_path))
    new_topic('Check existing path with os.path.exists()', True)
    print(os.path.exists(file_path))
    file_path = 'D:\\Temp\\Python'
    new_topic('Check if it a directory os.path.isdir()', True)
    print(os.path.isdir(file_path))
    new_topic('Check if it a file os.path.isfile()', True)
    print(os.path.isfile(file_path))
    new_topic('Split extension with os.path.splitext()', True)
    file_path = os.path.join(os.environ.get('PYTHON_TEMP'), 'test.txt')
    print(os.path.splitext(file_path))

    end()
