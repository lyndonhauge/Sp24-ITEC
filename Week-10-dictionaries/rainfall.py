"""
practice program similar to snowfall program. Using many dictionary features to store data about
rainfall.
"""

months = ['June', 'July', 'August']

rainfall_per_month = {}

for month in months:  # looping over list to be able to print each month.
    rain = float(input(f'How much rain fell in {month}? '))
    rainfall_per_month[month] = rain


# print all the data
for month, rain in rainfall_per_month.items():  # looping over new and updated dictionary to display data
    print(f'In {month} it rained {rain} inches')

# total rain
total = sum(rainfall_per_month.values())
print(f'The total rain is {total} inches')

# average
number_of_months = len(rainfall_per_month)  # num of key-value pairs

average = total / number_of_months
print(f'The average for {number_of_months} months is {average} inches')
