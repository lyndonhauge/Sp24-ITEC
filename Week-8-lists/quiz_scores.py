"""
using user input to change a fake list of test scores
"""


quiz_scores = [8, 4, 10, 9, 7]

quiz = int(input('Which quiz did you retake? '))
index = quiz - 1  # needed because computer counts from zero so user input will be one above what it expects

score = int(input(f'What was your score on quiz {quiz}? '))  # user inputs new score for specific quiz.

quiz_scores[index] = score

print(quiz_scores)
