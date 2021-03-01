import time, random, pyinputplus as pyip

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    #  pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        #  right answer are handled by allowRegex
        #  wrong answer are handled by blockRegex, with custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=['.*', 'Incorrect'], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of Tries')
    else:
        # this block runs if no exceptions were raised in the try block
        print('Correct')
        correctAnswers += 1

    time.sleep(1) # Brief pause to let use see the result
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
