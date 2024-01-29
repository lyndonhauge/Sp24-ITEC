read_syllabus = input('Enter Y if you have read the syllabus for the class: ')

# using != means if the input is NOT that variable, do this
if read_syllabus.upper() != 'Y':
    print('Please read the syllabus, it has important information in it. Thanks!')

# adding .upper() at the end makes the input not be case-sensitive. (you can put lowercase y)
if read_syllabus.upper() == 'Y':
    print('Thanks for reading the syllabus!')
