import os
import copy

BOARD_SIZE = 8

#TODO: spróbować wrzucić

def next_move(board):
    """
    for row in reversed(range(8)):
        for col in range(8):
            if board[row][col] == 1:

                if row > 0 and no_opponent_win(board, row - 1, col):
                    # not the top row, check if not let the opponent win
                    print("Clicking:", row - 1, col)
                    return [row - 1, col]
                else:
                    # start getting rid of 0th row light or prevent your opponent win
                    print("Clicking:", 7, col)
                    return [7, col]

    """
    # MANUALLY
    print("Your next move: ", end = '')
    mv = [int(i) for i in input().strip().split()]
    return mv

def no_opponent_win(board, mv1, mv2): # either I win or the opponent won't win
    temp_board = copy.deepcopy(board)
    change_board(temp_board, [mv1, mv2])

    success = True
    for row in reversed(range(8)):
        for col in range(8):
            if temp_board[row][col] == 1:
                change_board(temp_board, [row - 1, col])
                success = False
                break
        if success == False:
            break
        else:
            return True

    for row in reversed(range(8)):
        for col in range(8):
            if temp_board[row][col] == 1:
                return True

    return False

def print_board(board):
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

def board_empty(board):
    for row in reversed(range(8)):
        for col in range(8):
            if board[row][col] == 1:
                return False

    return True

def change_board(board, mv):
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

while not board_empty(board):
    os.system("clear")
    print_board(board)
    mv = next_move(board)
    input()
    change_board(board, mv)

"""
00000000
00000000
00000000
00000000
00000000
00000000
11100011
00101000

POMYSŁY:
1) zbijaj lampki, jeżeli są jakieś poza 0. wierszem (kliknij nad 1)
2) jak po moim ruchu jest 1 ruch do wygranej, to zagraj inne losowe miejsce i do 1
3) strategia na zbicie 0. wiersza:
     dać w tej kolumnie na samej górze i zbijać dalej normalnie.
     WAŻNE, żeby iść od początku wiersza od ostatniego wiersza
"""
