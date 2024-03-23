"""
Lab question 2
Euro currency conversion program using a dictionary
"""

rates = {
    'AUD': 1.5311,
    'BGN': 1.9558,
    'BRL': 4.9682,
    'CAD': 1.3351,
    'CHF': 0.9863,
    'CNY': 7.0894,
    'CZK': 24.422,
    'DKK': 7.4419,
    'EUR': 1,
    'GBP': 0.87478,
    'HKD': 7.7493,
    'HRK': 7.5353,
    'HUF': 401.15,
    'IDR': 15491.81,
    'ILS': 3.5065,
    'INR': 81.02,
    'ISK': 145.5,
    'JPY': 145.19,
    'KRW': 1397.7,
    'MXN': 19.2611,
    'MYR': 4.6872,
    'NOK': 10.2019,
    'NZD': 1.6769,
    'PHP': 57.672,
    'PLN': 4.6825,
    'RON': 4.8893,
    'RUB': 86.7666,
    'SEK': 10.8538,
    'SGD': 1.3891,
    'THB': 36.906,
    'TRY': 18.3845,
    'USD': 0.9872,
    'ZAR': 17.7983
}

currency_name = input('Enter the currency code to exchange: ')  # asking the user to input 3-letter code

exchange_rate = rates.get(currency_name)  # using .get to check if currency is in the dictionary and send None if not.

while exchange_rate is None:  # this while loop makes it so for as long as the currency isn't in the dictionary they can try again.
    print('This conversion cannot be done.')
    currency_name = input('Enter the currency code to exchange: ')
    exchange_rate = rates.get(currency_name)  # (reassigning the exchange rate based off of new input)

euro_to_convert = float(input('How many Euros to convert? '))  # user input for the # of euros to convert.

print(f'The exchange rate is {exchange_rate}')  # telling the user the exchange rate assigned from the dictionary

exchanged_currency_amount = euro_to_convert * exchange_rate  # doing the calculation with variables for equivalent
print(f'The equivalent in that currency is {exchanged_currency_amount:.3f} ')  # printing equivalent
