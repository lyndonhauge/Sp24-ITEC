answer = input('What is the state capital of Wisconsin? ')    # it's Madison

while answer.upper() != 'MADISON':
    print('Sorry, that is not right. Please try again')  # This loop will tell them they got it wrong and prompt them
    # to answer again until they get it correct.
    answer = input('What is the state capital of Wisconsin? ')

if answer.upper() == 'MADISON':  # This is for when the user gets the correct answer it'll print correct and end program
    print('Correct!')
