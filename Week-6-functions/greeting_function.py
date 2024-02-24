def greeting(name):
    message = f'Hello {name}'
    return message

def main():
    username = 'Lyndon'
    hello_message = greeting(username)
    print(hello_message)

main()

# when python runs this code, the first thing it does is quickly gaze over the two functions on top,
# make a record that they exist, and then it goes again and waits for those functions to actually be called.
# Once one of them are called (like in the line saying main()), it will actually go in to the code inside
# the function and start running that.

# The order that you define your functions in does not matter. so this code could have main at the top
# (makes a bit more sense to me that way I think. because that's the order that it goes in)

# The order that you call your functions in does matter though.
