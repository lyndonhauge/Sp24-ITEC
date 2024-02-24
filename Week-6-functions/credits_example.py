"""
This program is an example of how parameters carry over between functions in the specific order they are called
It shows how many credits the user needs to graduate using a report function.
"""


def main():
    credits_completed = int(input('How many credits have you completed? '))
    college = (input('What college are you currently enrolled in? '))
    report(credits_completed, college)  # calling report function with arguments in correct order.


def report(cr, col):
    print('Your school is', col)  # using the college variable with a changed name.
    print(f'You need {60 - cr} credits to graduate with an associates')


main()
