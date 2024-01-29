number_of_cents = int(input('How many pennies do you have? Enter here: '))
# here I am storing the answer they give as an int number in the variable number_of_cents above

# if statement will print you have less than a dollar if the amount given for number_of_cents is less than 100
# elif is like the next option, if they enter exact 100 it'll print the statement I gave.
# and else is the last option, it'll only get there if the other two don't work, and it'll work for values > 100
if number_of_cents < 100:
    print('You have less than a dollar')
elif number_of_cents == 100:
    print('You have exactly one dollar')
else:
    print('You have more than one dollar')
