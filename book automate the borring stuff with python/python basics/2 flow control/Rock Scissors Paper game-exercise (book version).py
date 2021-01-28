import random, sys

print('rock, paper, scissors')

# these variables keep track of the number of wins, losses, and ties
wins = 0
loses = 0
ties = 0

while True: # the main game loop
    print('%s Wins, %s Loses %s Ties' %(wins, loses, ties))
    while True:  # the player input loop
        print('enter your move: (r)ock (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # break out of the player input loop
        print('type one of r, p, s, or q.')

    # display what the player choose
    if playerMove == 'r':
        print('rock versus...')
    elif playerMove == 'p':
        print('paper versus...')
    elif playerMove == 's':
        print('scissors versus...')

    # display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('scissors')

    # display and record the wins=/loss/tie:
    if computerMove == playerMove:
        print('it is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('you win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('you lose!')
        loses = loses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('you lose!')
        loses = loses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('you lose!')
        loses = loses + 1