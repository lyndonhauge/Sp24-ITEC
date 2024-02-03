name = input('Enter your name here: ')  # asking for the user to input their name and storing it in the name variable

for letter in name:
    print(letter.upper())  # saying for each letter in the variable the loop will print a new line with an uppercase
    # letter and spell it out.

print(f'That was your name vertically {name}. Thanks for using this program!')  # using a fstring to thank the user
# with the name they originally entered.
