"""
cat facts api
"""

import requests

data = requests.get('https://catfact.ninja/fact').json()  # requesting and adding api to program/converting it from json
print(data)  # raw converted data will look and function just like a python dictionary
print()

fact = data['fact']  # calling the key for a cat fact and assigning it to a variable for easy use
print(f'A cat fact is: {fact}')
