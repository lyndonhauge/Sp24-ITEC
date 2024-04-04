"""
example using a much more complex api and pulling data from nested dictionaries.
uses weather data
"""

import requests

url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast'

response = requests.get(url).json()

properties = response['properties']
forecast_periods = properties['periods']

for period in forecast_periods:  # you can loop over forecast periods bc it's a list.
    name = period['name']
    temp = period['temperature']
    forecast = period['detailedForecast']
    print(f'{name}, {temp}F, {forecast}')  # human readable version of the data
#     example for presenting data in table format in lecture video
