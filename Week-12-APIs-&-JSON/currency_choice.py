"""
All currency exchange rates with USD using api
User is able to choose their code like with previous lab
"""

import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD'

response = requests.get(url).json()

rates = response['rates']

dollars = float(input('Enter the number of dollars: '))

print('Here are the currency codes:')
print(', '.join(rates.keys()))  # prints out all the different keys (exchange codes)
currency_code = input('Enter currency code to convert to: ')

exchange_rate = rates.get(currency_code)  # will look up the value for the code they enter

if exchange_rate:  # (if True)
    converted_value = dollars * exchange_rate
    print(f'${dollars} is equivalent to {converted_value:.2f} {currency_code}')
else:
    print('Not a valid currency code.')
