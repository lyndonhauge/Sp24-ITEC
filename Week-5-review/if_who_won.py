team_1_score = int(input('What was team 1\'s score? '))
team_2_score = int(input('What was team 2\'s score? '))  # backslash makes it so I can put the apostrophe.

if team_1_score > team_2_score:
    print('Team one won')
elif team_2_score > team_1_score:
    print('Team two won')
else:
    print('It was a tie')
