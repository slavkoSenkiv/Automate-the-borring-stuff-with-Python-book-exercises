import random

capitals = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento',
            'Colorado': 'Denver',
            'Connecticut': 'Hartford',
            'Delaware': 'Dover',
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',
            'Idaho': 'Boise',
            'Illinois': 'Springfield',
            'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',
            'Kansas':'Topeka',
            'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta',
            'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',
            'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',
            'Montana': 'Helena',
            'Nebraska': 'Lincoln',
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord',
            'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck',
            'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',
            'Tennessee': 'Nashville',
            'Texas': 'Austin',
            'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier',
            'Virginia': 'Richmond',
            'Washington': 'Olympia',
            'West Virginia': 'Charleston',
            'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'
            }

for children in range(50):
    quizFile = open(f'quizFile#{children + 1}.txt', 'w')
    answerFile = open(f'answerFile#{children + 1}.txt', 'w')

    quizFile.write(f'date:\n\nname: \n\n')
    quizFile.write(f'{" " * 20}quiz variant #{children + 1}\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for question in range(50):
        correctAnswer = capitals[states[question]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'#{question + 1}. What is the capital of {states[question]}?\n')
        for options in range(4):
            quizFile.write(f'{"ABCD"[options]}. {answerOptions[options]}\n')
        quizFile.write('\n\n')

        answerFile.write(f'#{question + 1} - answer = {"ABCD"[answerOptions.index(correctAnswer)]}.{correctAnswer}\n')

quizFile.close()
answerFile.close()
