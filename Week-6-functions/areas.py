"""
Program that defines and uses a function to calculate rectangle areas
"""


def rectangle_area(height, width):  # Two parameters
    area = height * width
    return area


def main():
    rect_height = float(input('Enter height of rectangle: '))
    rect_width = float(input('Enter width of rectangle: '))
    calculated_area = rectangle_area(rect_height, rect_width)  # Call function with two arguments

    print(f'The area of this rectangle is {calculated_area}')


main()
