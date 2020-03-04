import os

BOARD_SIZE = 8

def nextMove(board):
    """for row in reversed(range(8)):
        for col in range(8):
            if board[row][col] == '1':
                #not the top row
                if row > 0:
                    print(row - 1, col)
                    return"""
    print("Your next move: ", end = '')
    mv = [int(i) for i in input().strip().split()]
    return mv

def printBoard(board):
    for i in range(-1, 8):
        if i == -1:
            print(' ', end = ' ')
            continue
        print(f"\033[1;32;40m{i}\033[0m", end = ' ')
    print()

    for i in range(8):
        print(f"\033[1;32;40m{i}\033[0m", end = ' ')
        for j in range(8):
            print(board[i][j], end = ' ')
        print()

def boardIsEmpty(board):
    for row in reversed(range(8)):
        for col in range(8):
            if board[row][col] == 1:
                return False

    return True

def changeBoard(board, mv):
    board[mv[0]][mv[1]] = (board[mv[0]][mv[1]] + 1) % 2

    if mv[0] != 7:
        board[mv[0] + 1][mv[1]] = (board[mv[0] + 1][mv[1]] + 1) % 2
    if mv[1] != 7:
        board[mv[0]][mv[1] + 1] = (board[mv[0]][mv[1] + 1] + 1) % 2

#Read the board now. The board is a 8x8 array filled with 1 or 0.
print("Paste the initial board:")
board = []
for i in range(8):
    board.append([int(i) for i in input()])

while not boardIsEmpty(board):
    os.system("clear")
    printBoard(board)
    mv = nextMove(board)
    changeBoard(board, mv)

"""
00010011
00010000
00000000
00000000
00000000
00000000
00000000
00000000

POMYSŁY:
1) zbijaj lampki, jeżeli są jakieś poza 0. wierszem (włącz nad 1)
2) jak po moim ruchu jest 1 ruch do wygranej, to zagraj inne losowe miejsce i do 1
3) strategia na zbicie 0. wiersza:
    *) 1|
       0|
     dać w tej kolumnie na samej górze i zbijać
    a) .1. CHYBA JEDYNY SPECJALNY PRZYPADEK (. znaczy cokolwiek)
     dać w tej kolumnie na samej górze i zbijać dalej normalnie.
     WAŻNE, żeby iść od początku wiersza od ostatniego wiersza
"""
