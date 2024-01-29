answer = input('What is the state capital of Wisconsin? ')    # it's Madison

# Another way of doing this could be making the if statement pick up when
# it's wrong and swapping it (making the else say correct)
if answer.upper() == 'MADISON':
    print('Correct!')
else:
    print('The capital of Wisconsin is Madison')
