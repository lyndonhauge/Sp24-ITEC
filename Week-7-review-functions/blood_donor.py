"""
Using functions to recreate the blood donor program
"""

# to donate blood, you must be 17 or older, and weight must be 110 lbs or greater.


def main():
    # interacting with user
    age = int(input('Please enter your age, in years: '))
    weight = int(input('Please enter your weight, to the nearest pound: '))

    eligible = check_donor_eligibility(age, weight)  # calling function (don't need to be same words)

    if eligible:  # bool will store True or False
        print('You are eligible')
    else:
        print('Sorry, you are not eligible')


def check_donor_eligibility(age, weight):  # keeping arguments and parameters same for this example (don't need to)
    # make decision
    if age >= 17 and weight >= 110:
        return True
    else:
        return False


main()
