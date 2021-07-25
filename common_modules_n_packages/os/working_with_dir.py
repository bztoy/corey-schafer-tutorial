from utilities import (space, separated, start, end, sub, new_topic)
import os
from datetime import datetime

# Key
key = 'modules_os_dir_and_navigation'


def comeback():
    # goback to project working dir
    os.chdir('D:\\Programming\\Python\\Corey_Schafer_Tutorial')


def run():
    start('Modules and Packages')

    sub('Directory Management and Navigation')
    new_topic('dir() function')
    print(dir(os))
    new_topic('get current working dir with os.getcwd()', True)
    print(os.getcwd())
    new_topic('Navigate to new working directory os.chdir()', True)
    os.chdir('D:\\Programming\\Python')
    print(os.getcwd())
    # comeback to project working dir
    comeback()
    new_topic('List directory with os.listdir()', True)
    print(os.listdir())
    new_topic('Create a new directory with os.mkdir() and os.makedirs', True)
    # go to a temp foloder
    os.chdir('D:\\Temp\\Python')
    # os.mkdir will create the top level
    os.mkdir('dir1')
    # os.makedirs will be created both the top and its sub dirs immediately
    os.makedirs('dir2/sub_dir')
    print(f'current objs in the dir: {os.listdir()}')
    new_topic('Create a new directory with os.rmdir() and os.removedirs', True)
    # os.rmdir will delete only the top level
    os.rmdir('dir1')
    # os.removedirs will be deleted both the top and its sub dirs immediately
    os.removedirs('dir2/sub_dir')
    print(f'current objs in the dir: {os.listdir()}')
    # new_topic('Create a new file', True)
    new_topic('Rename a file with os.rename()', True)
    print(f'current objs in the dir: {os.listdir()}')
    # os.rename('test.txt', 'test_rename.txt')
    print(f'current objs in the dir: {os.listdir()}')
    new_topic('Check file stat with os.stat()', True)
    print(os.stat('test_rename.txt'))
    print(os.stat('test_rename.txt').st_size)
    print(f'modified at: {os.stat("test_rename.txt").st_mtime}')
    mod_time = os.stat('test_rename.txt').st_mtime
    print(f'modified at: {datetime.fromtimestamp(mod_time)}')
    new_topic('list all objects with os.walk()', True)
    current_dir = os.getcwd()
    # current path is the starting point
    for dirpath, dirnames, filenames in os.walk(current_dir):
        print('Current Path:', dirpath)
        print('Directories:', dirnames)
        print('Files', filenames)

    comeback()

    end()
