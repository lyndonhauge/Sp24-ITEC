from urllib import request
from time import sleep
url = 'https://www.google.com'
seconds_to_sleep_between_checks = 3

while True:
    print('Checking if online....')  # infinite loop
    try:
        request.urlopen(url).read()
        print('You are probably online!')
    except:
        print('You are not online')

    print(f'Sleeping for {seconds_to_sleep_between_checks} seconds')
    print()
    sleep(seconds_to_sleep_between_checks)

# instructions in video showing how to make it create sounds when you are online
