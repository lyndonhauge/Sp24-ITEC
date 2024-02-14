print('Hello, welcome to the houseplant recommendation program.')
temperature = input('Is your house warm or cool? Enter "warm" or "cool": ')
sun_or_shade = input('Does your house have sun or shade inside? Enter "sun" or "shade": ')

temperature = temperature.title()
sun_or_shade = sun_or_shade.title()  # making it so that the variables are uppercase no matter what, so no issues with
# it not matching the correct answer.

if temperature == 'Cool' and sun_or_shade == 'Shade':
    print('I recommend the Ivy Plant')
elif temperature == 'Cool' and sun_or_shade == 'Sun':
    print('I recommend the Jade Plant')
elif temperature == 'Warm' and sun_or_shade == 'Shade':
    print('I recommend the Begonia Plant')
elif temperature == 'Warm' and sun_or_shade == 'Sun':
    print('I recommend the Hibiscus Plant')
else:
    print('Sorry, I cannot recommend a plant, try again and make sure to enter the exact words provided.')
