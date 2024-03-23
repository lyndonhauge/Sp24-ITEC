"""
Dictionaries containing lists,
using the max and min function on lists to view students highest and lowest scores.
"""

quiz_scores = {
    'Al': [8, 9, 5],
    'Bettina': [6, 10, 10],
    'Cody': [7, 7, 9]
}

# Loop
for student, list_of_scores in quiz_scores.items():
    print(f'Student {student} scores are {list_of_scores}')

# Get one list
cody_scores = quiz_scores['Cody']
# cody_scores is a list - can do all the list operations

for i, score in enumerate(cody_scores):
    print(f'On quiz {i + 1} Cody scored {score}')

cody_max = max(cody_scores)
print(f'Cody\'s best score is {cody_max}')  # returning the largest number from cody list

bettina_scores = quiz_scores['Bettina']
bettina_min = min(bettina_scores)
print(f'Bettina\'s lowest score is {bettina_min}')  # returning the smallest number from bettina list
