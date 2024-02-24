def main():
    string = input('Please enter a string: ')
    repeat = int(input('How many times to repeat? '))
    result = string_repeater(string, repeat)  # these match with text and n in that order.
    print(result)


def string_repeater(text, n):  # todo WHEN BRINGING MULTIPLE VARIABLES OVER, THE ORDER THAT THEY ARE IN MAKES THEM MATCH
    repeated_string = text * n
    return repeated_string  # this data is returned into the result variable in main


main()
