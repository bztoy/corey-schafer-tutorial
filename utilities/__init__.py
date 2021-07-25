def space():
    print('')


def start(subject=''):
    start_with = '#==============================================#'

    space()
    print(start_with)
    if bool(subject and subject.strip()):
        print(subject)
        print(start_with)


def sub(text):
    print(text)
    separated()


def new_topic(text, bfsep=False):
    if bfsep == True:
        separated()
    print(text)


def end():
    print('#..............................................#')
    space()


def separated():
    print('#----------------------------------------------#')
