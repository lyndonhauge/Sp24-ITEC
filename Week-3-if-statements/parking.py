parking_time = float(input('How many hours have you parked? '))

# The max parking time allowed is 2 hours

# both > or >= are options for this.
# else means every answer given that doesn't fit the if statement.
if parking_time >= 2:
    print('Warning! You should move your car.')
    extra_time = parking_time - 2
    print('You have parked ' + str(extra_time) + ' hours over the limit')

else:
    print('You are ok for parking, you still have time.')
    # Can you print how many hours are left?
    time_left = 2 - parking_time
    print('You have ' + str(time_left) + ' hours left.')
