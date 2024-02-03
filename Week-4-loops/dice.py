import random  # adding random variable to program so that it can randomly roll the dice

number_of_dice = int(input('How many dice to roll? '))

# print('about to roll ' + str(number_of_dice) + ' dice') todo: ctrl + / quickly comments or un-comments a line

print(f'About to roll {number_of_dice} dice.')  # you can put f before and then use curly brackets instead
# of having to add str separately like above (f strings)


for dice in range(number_of_dice):  # (range function is making it go however many times the user enters)
    dice_value = random.randint(1, 6)
    print(f'Dice {dice + 1} value is {dice_value}')  # using fstring here to print each dice value
    # (putting + 1 so each value is correct)
