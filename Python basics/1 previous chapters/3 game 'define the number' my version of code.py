import random
number = random.randint(1, 20)
print('define my guessed number between 1 and 20 in 6 guesses')

for guessedNumber in range(1, 6):
    guessedNumber = int(input())

    if guessedNumber < number:
        print('your guess is to low')
    elif guessedNumber > number:
        print('your guess is too high')
    else:
        break

if guessedNumber == number:
    print('finnaly')
else:
    print('you are out of guesses')







