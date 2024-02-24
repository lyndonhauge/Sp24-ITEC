"""
Lab question 2
This program asks two example questions and uses the quiz function to do that + check if correct.
Main function stores strings and calls the quiz function.
"""


def main():
    question_1 = 'Which planet is closest to the sun? '
    answer_1 = 'Mercury'
    quiz(question_1, answer_1)  # calling the quiz function and using these strings for the argument and parameter
    question_2 = 'Who painted the Mona Lisa? '
    answer_2 = 'Leonardo da Vinci'
    quiz(question_2, answer_2)  # calling the quiz function and using these new strings for the argument and parameter


def quiz(quiz_question, correct_answer):
    user_answer = input(quiz_question)  # asks the user the specific question stored in the variable.
    if user_answer.upper() == correct_answer.upper():  # This part checks if the answer is the same and also uses upper
        print('Correct!')
    else:
        print(f'The correct answer is {correct_answer}.')  # tells the correct answer if the user was wrong.


main()  # calling the main function.
