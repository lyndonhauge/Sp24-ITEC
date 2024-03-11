"""
Starting with an empty loop and using a while true to allow the user to add tasks to it.
This program uses append to add the users input and stops the loop if bool False
"""


todo_list = []  # Start with an empty list.

while True:
    task = input('Enter your task, or press enter to stop: ')
    if task:  # if there are any characters in the string it'll stay true.
        if task in todo_list:  # this will check if they already added that task to the list.
            print('You already added that task')
        else:
            todo_list.append(task)  # adds new task to the end of the list each time user inputs when it runs.
    else:
        break  # empty string is False, will end the loop when user presses enter.

print('Thank you. Your tasks are:')

for index, task in enumerate(todo_list):  # enumerate version of loop prints the order of each task
    print(f'Task {index+1} is {task}')

number_of_tasks = len(todo_list)  # using len to count the amount of tasks to do. (however much the user input)
print(f'You have {number_of_tasks} tasks')  # can also just put len inside fstring without variable step.
