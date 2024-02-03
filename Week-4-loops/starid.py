star_id = input('Enter your StarID: ')

while len(star_id) != 8:  # Basically just while this condition is being met, continue printing this loop 
    print('Error - a valid StarID has 8 characters')
    star_id = input('Enter your StarID: ')

print('Thank you, your StarID is ' + star_id)
