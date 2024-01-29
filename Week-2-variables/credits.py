credits_taken = int(input('How many credits are you taking? '))
print(credits_taken)

credits_taken_last_semester = int(input('How many credits did you take last semester? '))
# the int before input converts answer given into int value instead of string

print(credits_taken_last_semester + credits_taken)

total_credits = credits_taken_last_semester + credits_taken

# converting the total credits back to string to print because they're int now
print('The total credits will be ' + str(total_credits) + ' in this and last semester')
