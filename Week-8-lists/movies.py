"""
Practicing the different ways that lists can be organized / printed out / manipulated.
"""
import random

movies = ['Fargo', 'Up', 'Rocky', 'Jaws']
print(movies)

movies.sort()
movies.reverse()
print(movies)  # printing the movies in reverse alphabetical order

for movie in movies:
    print(movie)  # printing them out in a row, still in the reverse alphabetical

movies_string = ', '.join(movies)  # joining them together into a string in this variable
print(movies_string)

movies.append('Scott Pilgram')  # adding another to the end of the list.
print(movies)

number_of_movies = len(movies)  # counts the amount of elements in the list.
print(f'there are {number_of_movies} movies in this list.')

movies.remove('Rocky')  # can use .remove to remove a specific thing from the list.
print(movies)

first_movie = movies.pop(0)  # pop will remove and return the item its removing.
# (removes it based off of where it is in the list)
print(movies)
print(first_movie)  # 'Up' will be returned into first_movie variable, so it'll print here.

last_movie = movies.pop()
print(movies)
print(last_movie)  # removes the last item on the list and stores it in the variable assigned

movies.append('Nemo')  # adding another movie so it'll shuffle.
random.shuffle(movies)
print(movies)  # printing newly shuffled list

for number, movie in enumerate(movies):  # lists in order vertically
    print(f'{number+1}: {movie}')
