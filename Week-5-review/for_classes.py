number_of_classes = int(input('How many classes are you taking? '))

class_names = ''  # empty string

for class_name in range(number_of_classes):
    name = input('Enter the name of a class you are taking: ')
    class_names = class_names + name + '\n'  # new line

print('Thank you, here are the classes you are taking: \n')
print(class_names)  # printing out the class names string once it's fully built.
