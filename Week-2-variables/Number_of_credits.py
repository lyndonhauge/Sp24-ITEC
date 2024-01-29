# I use a variable here to store the name of the person answering
name = input('Hello, what is your name? ')

# Here I use their name while also asking how many credits they're taking and storing that as an int variable as well.
credits_taking = int(input('Hello ' + name + ', how many credits are you taking this semester? '))

# Here I put an empty print just to space it out a bit for the final message which states the persons name,
# along with how many credits they are taking this semester using the variables. (converting int to string)
print()
print(name + ' is taking ' + str(credits_taking) + ' credits this semester')
