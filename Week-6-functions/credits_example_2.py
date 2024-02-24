"""
student status program with validation.
uses a third function and while not loop for checking if a user gives invalid input.
"""


def main():
    credit_count = int(input('Please enter the number of credits this semester: '))

    while not credits_valid(credit_count):  # (While not True) when the user gives invalid input.
        print('That is not a valid number of credits.')
        credit_count = int(input('Please enter the number of credits this semester, between 0 and 24: '))

    status_message = full_time_part_time(credit_count)  # string will be stored in status.

    print(f'Your status is a {status_message} student. ')


def credits_valid(credit_count):  # This function checks if the input of number of credits was right.
    if credit_count < 0 or credit_count > 24:
        return False
    else:
        return True


def full_time_part_time(credit_count):  # This function finds the users status as a student.
    if credit_count >= 12:
        return 'full time'
    elif credit_count >= 6:
        return 'part time'
    else:
        return 'less than part time'
    # This function will return a string for main to print in the end. 


main()
