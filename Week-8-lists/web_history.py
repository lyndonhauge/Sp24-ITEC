"""
This program uses the pop function to show how browsing history is held on to in case
a user presses the back button and revisits it. using pop without an argument inside it returns
the last value in a list.
"""


history = []

# Visiting example pages
history.append('www.google.com')
history.append('www.minneapolis.edu')
history.append('www.stackoverflow.com')

print(history)

# Pressing the back button
print(history.pop())  # returning the last thing in the list
print(history.pop())
print(history.pop())

print(history)  # it is empty now.
