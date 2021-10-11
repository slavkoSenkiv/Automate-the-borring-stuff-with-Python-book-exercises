# last repeat 12.02.21

import random

playerWins = 0
computerWins = 0
ties = 0
moves = 0

while True:
    print('enter your figure')
    player = input()
    if player == 'r' or player == 's' or player == 'p':
        computerGuess = random.randint(0, 2)
        if computerGuess == 0:
            computer = 'r'
        if computerGuess == 1:
            computer = 's'
        if computerGuess == 2:
            computer = 'p'
        print('vs ' + computer)

        # game logic here
        if player == 'r' and computer == 'r':
            ties += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))
        if player == 's' and computer == 's':
            ties += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))
        if player == 'p' and computer == 'p':
            ties += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))

        if player == 'r' and computer == 's':
            playerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))
        if player == 'r' and computer == 'p':
            computerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))

        if player == 's' and computer == 'p':
            playerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))
        if player == 's' and computer == 'r':
            computerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))

        if player == 'p' and computer == 's':
            computerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))
        if player == 'p' and computer == 's':
            playerWins += 1
            moves += 1
            print('C: ' + str(computerWins) + '. P: ' + str(playerWins) + '. T: ' + str(ties))

    else:
        print('enter the right figure')

    if playerWins == 3 or computerWins == 3:
        if playerWins > computerWins:
            print('Player won in ' + str(moves) + ' moves')
            break
        if computerWins > playerWins:
            print('Computer won in ' + str(moves) + ' moves')
            break



