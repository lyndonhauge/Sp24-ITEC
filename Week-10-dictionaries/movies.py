"""
Movies stored together with their ratings in a dictionary. keys are the movies and values are the ratings
"""


movies_ratings = {  # curly braces define dictionary, it's spaced out on many lines for more clarity/organization
    'Juno': 9,
    'My neighbor Totoro': 8,
    'Fantastic mr fox': 8,
}

juno_rating = movies_ratings['Juno']  # assigning the value (rating) from the dictionary into a variable to print
print(juno_rating)

# todo if you're unsure if a key exists, using .get() will make it return 'None' if it's not in the dictionary.
# it will also assign the value just as normal if the key actually is there.
batman_rating = movies_ratings.get('Batman')
print(batman_rating)

if batman_rating is None:
    print('There is no rating for Batman in the dictionary.')
else:
    print('there is a rating for batman, and it is ' + str(batman_rating))  # (if a rating is added)

# another way to check if a key is inside a dictionary.
if 'Up' in movies_ratings:
    print('Up is one of the movies')
#     (could add else)


movies_ratings['Juno'] = 10  # updating the value to a new rating by reassigning it like this.
print(movies_ratings)

# the way you update a key/value is the same as how you add a new one.
movies_ratings['Blue valentine'] = 9  # adding a new movie (key) and assigning it a rating (value)
print(movies_ratings)


for movie in movies_ratings:  # loop will print each key by default.
    # rating = movies_ratings[movie]  is another way to get each value (less common)
    print(movie)
#   print(rating)

for rating in movies_ratings.values():  # loop will print values using .values()
    print(rating)

for movie, rating in movies_ratings.items():  # loop will print both the key and value using .items()
    print(f'{movie} is rated {rating} out of 10')


# removing a key-value pair from the dictionary with pop, but also storing the value in a new variable.
mr_fox_rating = movies_ratings.pop('Fantastic mr fox')
print(mr_fox_rating)  # printing the variable with the value (rating) of the key (movie)

if 'The Avengers' in movies_ratings:  # can use if to make pop only remove something if it's there (stops error)
    movies_ratings.pop('The Avengers')  # todo could be useful inside a loop

