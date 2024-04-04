"""
Part 1 of lab assignment
Two tables that display bus times using apis
(northbound and southbound)
"""

import requests  # importing requests to use later

north_url = 'https://svc.metrotransit.org/NexTrip/17940?format=json'  # adding both apis to the program
south_url = 'https://svc.metrotransit.org/NexTrip/17928?format=json'

north_response = requests.get(north_url).json()  # requesting and converting both from json into their own variables
south_response = requests.get(south_url).json()


def table_maker(response):  # function creating the tables so that I don't have to write the code twice.
    departure_list = response['departures']  # assigning the list from the api so that I can use it easier later on.

    for check in departure_list:  # small loop with the purpose of assigning 0 or 1 to direction variable
        direction = check['direction_id']  # (direction id is either 1 or 0)
    if direction == 0:
        direction_text = 'Northbound'  # this is probably a sloppy way of doing this, but it works
    elif direction == 1:
        direction_text = 'Southbound'  # (direction_text variable is for use in the tables showing north/south)

    print()
    print(f'{direction_text} buses arriving on Hennepin Avenue outside Minneapolis College Campus')
    print('Route       Time           Route Description')  # this bit is just for visuals, will display once each table
    print('==============================================')
    for bus in departure_list:  # looping over the list of dictionaries(busses) in the api
        route = bus['route_id']
        time = bus['departure_text']  # these three lines are calling the data from each bus and assigning it
        description = bus['description']
        print(f'{route:<12}{time:<15}{description}')  # format string printing each bit of data to fit the table.
    print('==============================================')


table_maker(north_response)  # calling the function twice, once for each api (north and south)
table_maker(south_response)
