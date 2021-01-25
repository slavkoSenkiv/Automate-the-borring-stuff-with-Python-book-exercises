import random, sys
print('lets play rock scissors papers game')

wins = 0
loses = 0
ties = 0

while True: #the main game loop
    print('%s wins %s loses %s ties' %(wins, loses, ties))


    while True: #player input loop
        print('enter (s)scissors, (r)ock (p)aper or (q)ite')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break
        print('enter r, s, p')

#player move
    if playerMove == 'r':
        print('rock versus...')
    if playerMove == 's':
        print('scissors versus...')
    if playerMove == 'p':
        print('paper versus...')

#computer move
    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('rock')
    if computerMove == 2:
        computerMove = 's'
        print('scissors')
    if computerMove == 3:
        computerMove = 'p'
        print('paper')

#game logic
    if playerMove == 'r' and computerMove == 'r':
        print('it is tie')
        ties = ties + 1
    if playerMove == 'r' and computerMove == 's':
        print('it is win')
        wins = wins + 1
    if playerMove == 'r' and computerMove == 'p':
        print('it is lose')
        loses = loses + 1

    if playerMove == 's' and computerMove == 'r':
        print('it is lose')
        loses = loses + 1
    if playerMove == 's' and computerMove == 's':
        print('it is tie')
        ties = ties + 1
    if playerMove == 's' and computerMove == 'p':
        print('it is win')
        wins = wins + 1

    if playerMove == 'p' and computerMove == 'r':
        print('it is wins')
        wins = wins + 1
    if playerMove == 'p' and computerMove == 's':
        print('it is lose')
        loses = loses + 1
    if playerMove == 'p' and computerMove == 'p':
        print('it is tie')
        ties = ties + 1


