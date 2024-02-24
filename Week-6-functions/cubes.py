def main():
    for number in range(10):
        c = cube(number)
        print(c)

def cube(value):
    cubed_value = value * value * value  # putting ** and then a number will make a value multiply by itself that many times
    return cubed_value

main()  # output is a list of the cubed values of numbers 1-9
