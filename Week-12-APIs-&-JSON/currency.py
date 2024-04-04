"""
euro currency exchange program (like last lab) but using api
"""

import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD&symbols=EUR'

dollars = float(input('Enter number of dollars: '))

response = requests.get(url).json()  # requesting api in response variable

rates = response['rates']  # calling specific 'rates' key from dictionary
print(rates)  # rates key contains another dictionary with the USD to EUR exchange rate.

exchange_rate = rates['EUR']  # can use the variable just created to call down the nested dictionary.
print(exchange_rate)

exc_rate = response['rates']['EUR']  # second way to do it without making extra variable
print(exc_rate)  # (same number as exchange_rate, quicker way of getting it)


euros = dollars * exchange_rate  # (could also use exc_rate)
print(f'${dollars} is equivalent to {euros:.3f} euros.')
