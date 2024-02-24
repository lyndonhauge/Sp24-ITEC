"""
Lab question 3
This program checks if a user is able to upgrade to Windows 11 using the can_upgrade function.
Uses bool because it's a matter of yes or no
"""


def main():  # main asks the users the questions and stores data given inside the variables
    memory = int(input('How many GB of memory does your computer have? '))
    storage_space = int(input('How many GB of free storage space does your computer have? '))
    os = input('What is the name of your current operating system? ')

    eligible = can_upgrade(memory, storage_space, os)  # calls the can_upgrade function to check eligibility.

    if eligible:
        print('You can upgrade to Windows 11!')  # This will print if bool True.
    else:
        print('You cannot upgrade to Windows 11, you need at least 8GB memory, 64GBs of free space, and \n'
              'must be running Windows 10 :(')  # This will print if not.


def can_upgrade(memory_amount, free_storage, os_running):  # changing variable names (not really needed)
    if memory_amount >= 8 and free_storage >= 64 and os_running == 'Windows 10':  # requirements
        return True  # if everything matches up return the boolean True
    return False  # if not return false


main()  # call main.
