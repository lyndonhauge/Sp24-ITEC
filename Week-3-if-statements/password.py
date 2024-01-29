secret_password = 'kittens'

password = input('Enter the secret password: ')

if password == secret_password:
    print('Welcome, authorized user!')

# else will print this message if anything other than the if statement is posted.
else:
    print('sorry wrong password')
