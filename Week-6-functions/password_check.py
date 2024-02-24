"""
This program uses if statements inside functions to check if the length of a password is >= 8 and
send back a True or False value to main depending on the password given.

Different messages are printed depending on the bool value sent back.
"""


def main():

    password = input('Please type a password: ')
    if is_password_long_enough(password):  # This means if True.
        print(f'The password "{password}" is long enough.')
    else:
        print(f'The password "{password}" is NOT long enough.')


def is_password_long_enough(password):
    # Return True if password is at least 8 characters
    if len(password) >= 8:
        return True
    else:
        return False  # (if it is less than 8)


main()
