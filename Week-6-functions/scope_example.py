"""
This program shows why you need to put variables inside arguments and parameters, and why
it's important to pay attention to the scope that your variables are in.
        LOCAL or GLOBAL
"""


def main():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    calculate_volume()  # needs arguments and parameters inside () !


def calculate_volume():
    # This DOESN'T work  - the calculate_volume function
    # can't access variables from the main function. They are LOCAL to main.
    volume = length * width * height
    print(f'The volume of the box is {volume}')


main()
