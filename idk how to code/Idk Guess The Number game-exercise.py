# idk how to continue the game while user continue to enter srt values

"""
the output will look something like this:
I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!

"""

import random
randomNumber = random.randint(0, 20)
numberOfGuesses = 0

try:
    while numberOfGuesses <= 6:
        numberOfGuesses += 1
        print('guess a number! ' + 'You have ' + str(7 - numberOfGuesses) + ' guesses yet')
        guess = input()
        if int(guess) == randomNumber:
            print('you did it in ' + str(numberOfGuesses) + ' guesses')
            break
        elif int(guess) < randomNumber:
            print('the guessed number is higher')
        elif int(guess) > randomNumber:
            print('the guessed number is lower')
except ValueError:
    print('enter an integer')
