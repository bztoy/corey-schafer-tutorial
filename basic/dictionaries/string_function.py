def string():
    print("This string is from data")


def run():
    # Dict of Subjects (value is a function)
    subjects = {}
    subjects['string'] = string

    # Get input string
    text = input("Enter subject key: ").lower()

    if text == None:
        print("Enter subject key")
    else:
        if text in subjects:
            # Call a function
            subjects[text]()
        else:
            print(f"Key {text} not found")
