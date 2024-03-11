"""
Using the list from streets program along with a loop to print out delivery instructions
"""

streets = ['Lake', 'Hennepin', 'Lyndale']
print(streets)  # prints ['Lake', 'Hennepin', 'Lyndale']

for street in streets:
    print(street)  # will make it print each street vertically.

delivery_instructions = 'Please deliver to these streets: '

for street in streets:
    delivery_instructions = delivery_instructions + street + ', '

print(delivery_instructions)
