"""
Using functions to recreate the dice roll code
"""

import random


def main():
    # interact with user, gets number of dice
    number_of_dice = int(input('How many dice to roll? '))
    roll_dice(number_of_dice)  # calling function to roll dice. uses argument

    print('That was all the dice')


def roll_dice(dice):  # parameter value is set from argument number_of_dice
    # rolling the required number of dice
    for dice_count in range(dice):
        dice_roll = random.randint(1, 6)
        print(f'The dice rolled a {dice_roll}')


main()
