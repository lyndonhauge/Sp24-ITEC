"""
program written in lecture. brief showing of an api that shows updated exchange rates for bitcoin
"""

import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url).json()

print(response)

bpi = response['bpi']

print(bpi)


# another way to call a specific value without having to make each key have its own variable
usd_exchange_rate = response['bpi']['USD']['rate_float']
print(usd_exchange_rate)
