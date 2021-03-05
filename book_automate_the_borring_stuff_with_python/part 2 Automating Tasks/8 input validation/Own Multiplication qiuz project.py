import random, pyinputplus as pyip, time

numOfQuestions = 3
correctAnswers = 0

for question in range(numOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    try:
        answer = pyip.inputInt(f'#{question} {num1} * {num2} = ', timeout=10, limit=3)
        if answer == num1 * num2:
    except pyip.TimeoutException:
        print('you are out of time')
    except pyip.RetryLimitException:
        print('you are out of tries')
    else:
        correctAnswers += 1
        print('Correct')
        time.sleep(1)


print(f'your score is {correctAnswers}/{numOfQuestions}')


