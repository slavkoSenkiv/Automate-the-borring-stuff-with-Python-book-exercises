# This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('i am thinking if a number between 1 and 20')

# Ask the player to guess 6 times
for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is to high')
    else:
        break # this condition is the correct guess!

if guess == secretNumber:
    print('good job You guessed my number in ' + str(guessTaken) + ' guesses')
else:
    print('nope, the number i was thinking was' + str(secretNumber))

print()

