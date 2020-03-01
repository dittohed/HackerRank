def nextMove(player, board):

    for row in reversed(range(8)):
        for col in range(8):
            if board[row][col] == '1':
                #not the top row
                if row > 0:
                    print(row - 1, col)
                    return

player = int(input())

#Read the board now. The board is a 8x8 array filled with 1 or 0.
board = []
for i in range(8):
    board.append(input())

nextMove(player, board)
