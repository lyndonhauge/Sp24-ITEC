# • Invoice Program
# • Ask for the name of a product sold
item_name = input('What is the product name? ')

# • Ask how many were sold
items_sold = int(input('How many items were sold? '))
# • Ask for the price of one item
unit_price = float(input('How much does one item cost? '))

# • Do the math to figure out the total price
total = items_sold * unit_price

# • Print a neat invoice with all the data in
# • Comment code
print()
print(item_name + ' Sales')
print('Quantity Sold: ' + str(items_sold))
print('Unit Price: $' + str(unit_price))
print('Total: $' + str(total))
