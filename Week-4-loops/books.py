# Add up prices of all books for a semester

number_of_books = int(input('How many books to buy? '))

total = 0

for book in range(number_of_books):  # using number of books the user input as a range so that it asks that many times
    book_price = float(input('Enter book price in $ '))  # you can ask for input within a loop
    if book_price == 0:
        print('Free book!')
    total = total + book_price  # loop will add the books price to the total each time it runs through here.

print('The total price for all books is ' + str(total))  # could use fstring here too
# print(f'The total price for all books is {total}')
