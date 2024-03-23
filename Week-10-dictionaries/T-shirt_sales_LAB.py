"""
Lab question 1
program that saves T-shirt sales per day and does some analysis
"""

# creating list with all the days of the week for later use.
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

t_shirts_sold = {}  # empty dictionary which I will add sales with their days to.

for day in days_of_week:  # for loop which purpose is to add amount of sales to each day of the week.
    sales = int(input(f'How many T-shirts were sold on {day}? '))  # asking user input
    t_shirts_sold[day] = sales  # storing sales as a value for each key (the days)

total_sales = sum(t_shirts_sold.values())  # adding up all the values in the dictionary for a combined total

num_of_days = len(t_shirts_sold)  # counts the number of key/value pairs in the dictionary (# of days)
average = total_sales / num_of_days  # math to get the average using variables made.

print()
print(f'Total sales: {total_sales}, average per day: {average:.2f}')  # printing out average and total neatly
print()

for day, sales in t_shirts_sold.items():  # for loop which will print out information from the dictionary made.
    if sales > average:
        print(f'{day} sales: {sales} t-shirts ↑')  # each message will print under condition (comparing with average)
    elif sales == average:
        print(f'{day} sales: {sales} t-shirts =')  # I added an equal to instead of >= for ↑, hope that's fine
    elif sales < average:
        print(f'{day} sales: {sales} t-shirts ↓')
