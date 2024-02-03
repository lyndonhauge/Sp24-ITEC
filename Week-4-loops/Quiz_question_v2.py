answer = input('What is the state capital of Wisconsin? ')    # it's Madison
total_tries = 1  # setting up a variable to show the amount of tries the user attempts

while answer.upper() != 'MADISON' and total_tries < 3:  # other way of ending the loop I put before learning break
    print('Sorry, that is not right. Please try again')
    answer = input('What is the state capital of Wisconsin? ')  # prompt the user to change their answer (another chance
    total_tries = total_tries + 1  # each time they answer add on to the total tries.
    if total_tries >= 3:  # once they reach the max amount of tries the loop will break into this if statement.
        if answer.upper() != 'MADISON':  # had to add this extra if so it didn't print it if they got it right.
            print('Sorry, you ran out of guesses, the answer is "Madison"')
        break  # the other more simple option for stopping the loop if the condition above is met (from textbook)

if answer.upper() == 'MADISON':
    print(f'Correct! You got the answer in {total_tries} guess(es)')  # if the user gets it correct tell them how many
    # tries it took them using the total_tries variable.

    # could be done with for loop as well (probably more simply too)
