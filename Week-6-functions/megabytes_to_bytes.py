def main():  # main means that it will be the first function that runs.
    megabytes = int(input('Please enter the amount of megabytes: '))
    bytes = megabytes_to_bytes(megabytes)
    print(f'{megabytes} megabytes is equal to {bytes} bytes')

def megabytes_to_bytes(megabytes):  # todo WHEN BRINGING MULTIPLE VARIABLES OVER, THE ORDER THAT THEY ARE IN MAKES THEM MATCH
    bytes = megabytes * 1000000
    return bytes

main()  # continue videos - functions some more examples 5:19
