department_code = input('Enter the 4-letter department code: ')

while len(department_code) != 4:  # checking the length of the user input. 
    print()
    print('Sorry, the department code must be 4 letters')
    department_code = input('Enter the 4-letter department code: ')

print()
print(f'Thank you, you entered {department_code}')