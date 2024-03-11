"""
Introducing the different ways that lists can be organized and printed out.
"""


languages = ['Python', 'Java', 'JavaScript', 'C#', 'Swift']

for language in languages:
    print(language)  # prints each part of the list out as a loop would.

all_languages = ' * '.join(languages)
print(all_languages)  # prints all them out in a string

languages.sort()  # sorts list into alphabetical order
print(languages)  # will print the list in the new order.

languages.reverse()  # reverses the sorting just done.
print(languages)  # prints the list in reverse alphabetical order


languages.append('Kotlin')  # adds a new item to the list.
print(languages)
