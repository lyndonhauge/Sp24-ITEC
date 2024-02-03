import random

want_to_quit = ''  # empty string is "false" and the while not loop will reverse it to be "true"

while not want_to_quit:
    dice_value = random.randint(1,6)
    print(f'You rolled a {dice_value}')
    want_to_quit = input('Roll again? Press enter to roll again, any other key to quit. ')
    # if the user presses anything but enter it'll make the variable want_to_quit true (by not being empty), and the
    # while not will reverse it and make it false, making the loop not run anymore and the program finish
