# I start by asking them their name so the system seems more polite
username = input('Hello, welcome to the bus ride calculation service. What is your name? ')
# Then I ask them the amount of times they have rode the bus while transferring it to int because it's a whole number
times_rode = int(input('Hello ' + username + ', how many times did you ride the bus in the last month? '))
# I then ask how much each ride costs and store it as another variable to use later
cost = float(input('How much does one bus ride cost? '))

# Use the variables to calculate the total amount by multiplying the times rode by the cost of one ride
total = times_rode * cost
print()
# Print them all together and allow the variables to show by making them string
print('You rode the bus ' + str(times_rode) + ' times this month. One bus ride costs $' + str(cost) + ' Your total cost was $' + str(total))
print('Have a nice day ' + username + '!')
