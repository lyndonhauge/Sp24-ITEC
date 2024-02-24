"""
This program creates rectangles out of words and the amount of letters inside them.
Uses multiple functions and loops, and continues if the user wants. 
"""


def main():

    while user_wants_to_continue('make squares from words'):
        word = input('Please enter the word to print in a square: ')
        word_square(word)  # continue using this action function only while userwantstocontinue is still running.

    print('Thanks for using the program!')


def word_square(word):
    for letter in range(len(word)):
        print(word)


def user_wants_to_continue(task):  # putting the string make squares from words into task variable.
    response = input(f'Do you want to {task}? Enter "Y" for yes, anything else for no. ')
    # Uppercase the response, so "y" and "Y" are both equal to "Y".
    # This means the user can enter "Y" or "y".
    # This is a useful strategy for case-insensitive comparisons.
    if response.upper() == 'Y':
        return True
    return False  # (else return False)


main()
