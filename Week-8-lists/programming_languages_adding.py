"""
adding together two lists and then sorting them at the end.
Shuffling with random.
"""
import random

alice_languages = ['Kotlin', 'Swift']
bob_languages = ['Javascript', 'HTML', 'CSS']

team_languages = alice_languages + bob_languages
print(team_languages)

team_languages.sort()
print(team_languages)

random.shuffle(team_languages)
print(f'shuffled - {team_languages}')
