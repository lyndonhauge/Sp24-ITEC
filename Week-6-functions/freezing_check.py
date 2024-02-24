"""
This program shows how you can store return values (from function) in new variables and also use them later.
Tells the user if it will be freezing or not.
"""


def main():
    # Call the above_freezing function, in different ways

    today_temp = float(input('Please enter today\'s high temperature: '))
    # Call the function in a print statement
    print('It will be ' + above_freezing(today_temp) + ' today')

    tonight_temp = float(input('Please enter tonight\'s low temperature: '))
    # calling the function, saving the return value in a new variable, using it later in
    # the program in the print statement.
    above_below_tonight = above_freezing(tonight_temp)
    print(f'It will be ' + above_below_tonight + ' tonight')

    tomorrow_temp = float(input('Please enter tomorrow\'s high temperature: '))
    # Calling the function in an f-string
    print(f'It will be {above_freezing(tomorrow_temp)} tomorrow')

    print(f'\n'  # next line for spacing
          f'Today it will be {today_temp}, tonight it will be {tonight_temp}, and tomorrow \n'
          f'it will be {tomorrow_temp}.')
    print(f'\n'
          f'it will be {above_freezing(today_temp)} today, {above_freezing(tonight_temp)} tonight, \n'
          f'and {above_freezing(tomorrow_temp)} tomorrow')


def above_freezing(temp):
    if temp > 32:
        return 'above freezing'
    else:
        return 'below freezing'


main()
