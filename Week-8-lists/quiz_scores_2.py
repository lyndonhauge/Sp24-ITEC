"""
Uses same idea as first quiz scores program but includes a loop with range and multiplies
the number of quizes in the list at the start. 
"""


quiz_scores = [0] * 5
print(quiz_scores)

for quiz in range(5):
    score = int(input(f'Enter score for quiz {quiz+1}: '))  # getting user input on score of each quiz in order.
    quiz_scores[quiz] = score  # assigning the score to each spot in the list.

print('Your scores are: ')
print(quiz_scores)
