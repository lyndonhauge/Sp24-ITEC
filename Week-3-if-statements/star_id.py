star_id = input('Please enter your StarID: ')

star_id_length = len(star_id)

# You can use len on the variable input to judge the length, then use if to print different
# messages for when the length is correct, too long and too short.

if star_id:   # is this not an empty string
    print('you have entered a star id')   # they have entered text so TRUE
else:
    print('you have NOT entered a star id')   # nothing entered, FALSE


if len(star_id) == 8:
    print('Your starID is the correct length')
elif star_id_length > 8:
    print('Your starID is too long')
else:
    print('Your starID is too short')
