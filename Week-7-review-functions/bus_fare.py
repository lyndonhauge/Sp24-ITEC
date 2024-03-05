"""
Bus fare calculator
Rush hour and regular fairs
"""


def bus_ride_cost_calculator(fare_type):  # fare type is a string describing the type of trip.
    number_of_rides = int(input(f'How many times did you ride the bus paying {fare_type} fares? '))
    bus_fare = float(input(f'What is the cost of one {fare_type} bus ticket? $'))

    total_cost = number_of_rides * bus_fare

    print(f'You rode the bus {number_of_rides} times and each ride costs ${bus_fare:.2f}')
    print(f'Your total {fare_type} expense is ${total_cost:.2f}')  # :.2f makes it show two decimal places

    return total_cost  # return the total cost calculated to the main function (for final combined fare)


def main():
    print('Bus fare calculator program')

    total_regular_cost = bus_ride_cost_calculator('regular')
    total_rush_cost = bus_ride_cost_calculator('rush hour')  # functions make it so you can call it more times easily
    # for example calling it again here for special discount prices if needed.
    # bus_ride_cost_calculator('special discount')

    total_bus_expense = total_regular_cost + total_rush_cost  # adding the two times the functions ran together.

    print(f'Your total bus expense is ${total_bus_expense:.2f}')


main()
