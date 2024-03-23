"""
program showing dictionary of colleges and their addresses.
shows how pop will remove keys and values and how values will store into a variable if needed.
"""

colleges = {'Minneapolis College': '1501 Hennepin Avenue, Minneapolis',
            'Metro State': '100 E 7th St, St. Paul',
            'North Hennepin Community College': '7411 85th Ave N, Brooklyn Park',
            'Century College': '3300 Century Avenue N, White Bear Lake'}

for college in colleges:
    print(college)

# remove key-value pair with pop
colleges.pop('Metro State')
print(colleges)  # will print everything except metro state and its address.

# pop will return the value of the key, similar to how lists worked.
century_address = colleges.pop('Century College')  # storing the value in century_address
print(century_address)  # 3300 Century Avenue N, White Bear Lake
print(colleges)  # the key-value pair is still removed.


# pop with no arguments would not work like how it does with lists since there is no order to remove the last one.

# colleges.pop()   # error

# and you cannot delete a key that isn't in the dictionary
