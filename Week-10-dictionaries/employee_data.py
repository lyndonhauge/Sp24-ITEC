"""
Example of how dictionaries can efficiently store data and also have nested dictionaries within.
"""

employee_data = {
    'name': 'Cody Developer',
    'employee_number': 123456,

    'location': {  # (dictionary inside dictionary)
        'city': 'Minneapolis',
        'office': 'M.123',
        'telephone': '612-123-4567'
    },

    'roles': ['python developer', 'server administrator']
}

# How can you read and modify Cody's office?
# Change cody's office to M.400
employee_data['location']['office'] = 'M.400'

# print cody's phone number
print(employee_data['location']['telephone'])

# Add a new role for Cody
employee_data['roles'].append('web developer')

# show everything
for key, value in employee_data.items():
    print(f'{key}: {value}')

# or print(employee_data) would work, just want to show slightly more organized way
