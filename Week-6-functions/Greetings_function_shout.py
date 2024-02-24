"""
Lab question 1
greets the user in all caps and changes their name to all caps as well.
"""


def main():
    username = input('Please enter your name here: ')  # storing the username in a variable from their input
    hello_message = greeting(username)  # running greeting function to change their name to uppercase and add more
    print(hello_message)  # prints the complete message out.


def greeting(name):
    message = f'HELLO {name.upper()}!!!!'  # adds more to the string without changing the actual name (just upper)
    return message  # returns the new complete message back to main


main()  # call the function
