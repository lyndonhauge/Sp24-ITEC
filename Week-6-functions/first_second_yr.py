"""
This program uses a function that decides if a class code is first or second year.
"""


def main():
    class_code = int(input('Enter your class code: '))
    class_year = year_decider(class_code)  # running the function to check. making result store in variable class_year
    print(f'You are taking a {class_year} class.')


def year_decider(code):
    if 1000 <= code <= 1999:  # easier way to check that it falls in the middle without and statement.
        return 'First Year'
    elif 2000 <= code <= 2999:
        return 'Second Year'
    else:
        return 'Invalid code'


main()
