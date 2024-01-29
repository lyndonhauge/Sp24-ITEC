first = input("Enter first number ") # Here program will ask user to input first number
operator = input("Enter operator (+,-,/,*,%) :") # User have to make choice to use one of them
second = input("Enter second number : ") # Enter second number

first = float(first)
second = float(second)

if operator == "+":
    print(first + second) # If you choose '+' system will add both numbers
elif operator == "-":
    print(first - second)# If you choose '-' system will subtract one from another numbers
elif operator == "/":
    print(first / second)# If you choose '/' system will divide both numbers
elif operator == "*":
    print(first * second)# If you choose '*' system will multiply both numbers
elif operator == "%":
    print(first % second)# If you choose '%' system will convert to percentage numbers

else:
    print("Invalid Operation") # If you write something else than provided operators then it will print this
