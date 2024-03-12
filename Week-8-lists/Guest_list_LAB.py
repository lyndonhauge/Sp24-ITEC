"""
Lab question: Program to create and manage a guest list for an event or party.
Uses a bunch of list features.
"""
import random  # importing random to use later on in the code.

guest_list = []  # creating empty list for guest names

while True:  # while loop that runs as long as the user continues to give input.
    guest = input('Enter guest names one by one, or press enter to stop: ')
    if guest:
        if guest in guest_list:
            print('You already added that guest')  # if there is a duplicate it'll show this then start again
        else:
            guest_list.append(guest)  # if user gives a name it will be added
    else:
        break  # if user presses enter it'll end the loop.


def show_list():  # function that prints out an enumerated guest list
    print('The guests on the list are shown below.')
    for number, guest in enumerate(guest_list):
        print(f'{number + 1}: {guest}')


show_list()  # using the function right here

print()
want_to_delete = input('Enter "Y" if you want to delete a guest, and "N" if you are finished: ')  # giving the user the option if they want to remove.
if want_to_delete.upper() == 'Y':  # if yes it goes into the while loop
    while True:
        guest_to_delete = (input('Enter the name of the guest you would like to delete: '))  # while loop will ask them the specific name
        if guest_to_delete in guest_list:
            guest_list.remove(guest_to_delete)  # This will remove the name entered from the list.
            want_to_delete = input('Enter "Y" if you want to delete a guest, and "N" if you are finished: ')  # asks them again to repeat same process
            if want_to_delete.upper() != 'Y':  # break the loop if they no longer want to continue removing
                break
        else:
            print('Sorry, that wasn\'t on the list')  # restart if they didn't enter someone on the list


show_list()  # using the function created earlier.

print()  # space for organization

number_of_prizes = int(input('How many prizes will there be? '))  # storing the number of prizes for later use

prize_sample = random.sample(guest_list, number_of_prizes)  # using sample rather than choice because choice was making it very difficult to not have duplicates
winners_string = ', '.join(prize_sample)  # turning it into an easier to read string

print(f'The random prize winners are: {winners_string}')  # printing out the prize sample which contains a list of every randomized guest.
print()


# this last part is all organization for part 7.
num_of_guests = len(guest_list)  # counts up the number of elements in the list and puts it into a variable.
print(f'The total number of guests is {num_of_guests}')  # prints out that variable

show_list()  # using the same enumerated list function again.

print(f'{winners_string} will all be given a prize.')  # using the winners string again that I created on line 49.
