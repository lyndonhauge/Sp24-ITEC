# This loop will repeat the actions I put in it 31 times.
for number in range(31):
    day = number + 1  # making the days +1 because python starts counting at 0
    suffix = 'th'  # adding a default suffix that most of the numbers will have and not need to be changed.

    if day == 11 or day == 12 or day == 13:  # if statement making sure that 11,12,and 13 don't change (the exception)
        suffix = 'th'
    elif str(day).endswith('1'):
        suffix = 'st'
    elif str(day).endswith('2'):  # These elifs with the .endswith add on are checking if the days end with 1,2,or 3, and changing their suffix based off that.
        suffix = 'nd'
    elif str(day).endswith('3'):
        suffix = 'rd'

    print(f'January {day}{suffix}')  # printing out the final product of the day of the month and suffix combined

