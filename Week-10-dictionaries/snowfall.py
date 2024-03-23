"""
program that uses .items() and other things learned about dictionaries to print out data about
snowfall in winter months.
"""

winter_months = ['October', 'November', 'December', 'January', 'February', 'March', 'April']

snowfall = {}

for month in winter_months:
    snow = float(input(f'How much snow in {month}, in inches? '))
    snowfall[month] = snow  # assigning a key to each month every time the loop runs.

print()
print('Here is all of the data you entered: ')

for month, snow in snowfall.items():  # printing out the key (months) and values (snow) with .items
    print(f'In {month} there was {snow} inches of snow.')

# Analysis: what's the total amount of snow?

total_snow = sum(snowfall.values())  # calling all the values to sum them up and make it a variable

# Average snowfall per month - the total divided by the number of months
num_of_months = len(snowfall)  # (counting the number key/value pairs in the dictionary (months))
average = total_snow / num_of_months

print()
print(f'The total amount of snow in {num_of_months} months is {total_snow} inches.')
print(f'The average amount of snow per month is {average:.2f} inches')  # using formatting to keep it 2 decimal places
