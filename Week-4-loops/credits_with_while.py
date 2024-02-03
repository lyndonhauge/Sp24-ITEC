number_of_credits = int(input('How many credits are you taking this semester? '))

while number_of_credits < 0:
    print('Error - please enter 0 or a positive number')  # have to add something for them to change it after or it'll get stuck in the loop
    number_of_credits = int(input('How many credits are you taking this semester? '))  # ask them again to change variable

if number_of_credits >= 12:
    print('You are a full-time student')
elif number_of_credits >= 6:
    print('You are a half-time student')
else:
    print('You are a less than half-time')
