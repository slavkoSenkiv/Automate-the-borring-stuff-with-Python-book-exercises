
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printboard():
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



def gamelogic(dic, proces):

    while True: # X won crest
        if dic['top-L'] == 'X' and dic['mid-M'] == 'X' and dic['low-R'] == 'X':
            print('player X won')
            proces = False
        if dic['top-R'] == 'X' and dic['mid-M'] == 'X' and dic['low-L'] == 'X':
            print('player X won')
            proces = False

        # X won horizontal
        if dic['top-L'] == 'X' and dic['top-M'] == 'X' and dic['top-R'] == 'X':
            print('player X won')
            proces = False
        if dic['mid-L'] == 'X' and dic['mid-M'] == 'X' and dic['mid-R'] == 'X':
            print('player X won')
            proces = False
        if dic['low-L'] == 'X' and dic['top-M'] == 'X' and dic['top-R'] == 'X':
            print('player X won')
            proces = False

        # X won vertical
        if dic['top-L'] == 'X' and dic['mid-L'] == 'X' and dic['low-L'] == 'X':
            print('player X won')
            proces = False
        if dic['top-M'] == 'X' and dic['mid-M'] == 'X' and dic['low-M'] == 'X':
            print('player X won')
            proces = False
        if dic['top-R'] == 'X' and dic['mid-L'] == 'X' and dic['low-L'] == 'X':
            print('player X won')
            proces = False

        # O won crest
        if dic['top-L'] == 'O' and dic['mid-M'] == 'O' and dic['low-R'] == 'O':
            print('player O won')
            proces = False
        if dic['top-R'] == 'O' and dic['mid-M'] == 'O' and dic['low-L'] == 'O':
            print('player O won')
            proces = False

        # O won horizontal
        if dic['top-L'] == 'O' and dic['top-M'] == 'O' and dic['top-R'] == 'O':
            print('player O won')
            proces = False
        if dic['mid-L'] == 'O' and dic['mid-M'] == 'O' and dic['mid-R'] == 'O':
            print('player O won')
            proces = False
        if dic['low-L'] == 'O' and dic['top-M'] == 'O' and dic['top-R'] == 'O':
            print('player O won')
            proces = False

        # O won vertical
        if dic['top-L'] == 'O' and dic['mid-L'] == 'O' and dic['low-L'] == 'O':
            print('player O won')
            proces = False
        if dic['top-M'] == 'O' and dic['mid-M'] == 'O' and dic['low-M'] == 'O':
            print('player O won')
            proces = False
        if dic['top-R'] == 'O' and dic['mid-L'] == 'O' and dic['low-L'] == 'O':
            print('player O won')
            proces = False
        return proces


printboard()

game = True


while game:
    print('PlayerX move')
    playerX = input()
    board[playerX] = 'X'
    printboard()
    gamelogic(board, game)


    print('PlayerO move')
    playerO = input()
    board[playerO] = 'O'
    printboard()
    gamelogic(board, game)
else:
    print('the end')














