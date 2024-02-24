def main():
    miles = float(input('Please enter a number of miles: '))
    kilometers = miles_to_kilometers(miles)  # program goes down and runs the miles_to_kilometers function.
    print(f'{miles} miles is equal to {kilometers} kilometers.')


def miles_to_kilometers(miles):
    km = miles * 1.60934
    return km  # This function finishes and assigns the new value to the kilometers variable.


main()
