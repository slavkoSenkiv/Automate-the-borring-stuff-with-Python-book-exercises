import time, random, pyinputplus as pyip

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    #  pick two random numbers
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
