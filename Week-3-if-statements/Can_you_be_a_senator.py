# here I am asking the user questions and storing all of their answers as string and int variables
state_desired = input('Hello, what state do you want to be senator for? ')
state_living = input('What state are you currently living in? ')
age = int(input('How old are you? '))
citizen_years = int(input('How many years have you been a citizen of the United States? '))


# here I put the qualifications for becoming a senator all together and make it print that they are eligible if they are
# the and statements add on to the if statement and make all of the qualifications become one.
if state_living.upper() == state_desired.upper() and age >= 30 and citizen_years >= 9:
    print('You are qualified to become a senator in your state!')

# here I review the reasons they may not be eligible and tell them why they didn't qualify by using nesting ifs
else:
    print('You are not eligible')
    if state_living.upper() != state_desired.upper():
        print('You must live in the state you want to represent as senator')
    if age < 30:
        print('You must be at least 30 years old to be senator')
    if citizen_years < 9:
        print('You need to have been a United states citizen for at least 9 years to be senator')
