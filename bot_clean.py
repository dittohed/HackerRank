"""
b---d
-d--d
--dd-
--d--
----d

strategy: find the nearest one and go for it
"""

#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    calc_distances(posr, posc, board) #not the most efficient, but cheap enough
    b_r, b_c = closest(posr, posc, board)

    if b_r == posr and b_c == posc:
        return "CLEAN"
        board[b_r][b_c] = '-'
    else:
        diff_r, diff_c = b_r - posr, b_c - posc
        if diff_r > 0:
            return "DOWN"
        elif diff_r < 0:
            return "UP"
        elif diff_c > 0:
            return "RIGHT"
        elif diff_c < 0:
            return "LEFT"

def calc_distances(posr, posc, board): #fills board with distances instead of b chars
    for (i, j) in [(x, y) for y in range(5) for x in range(5)]:
        if board[i][j] == 'b':
            distance = abs(posr - i) + abs(posc - j)
            board[i][j] = distance

def closest(posr, posc, board): #returns pos of the closest b
    min = 8 #max initial distance

    for (i, j) in [(x, y) for y in range(5) for x in range(5)]:
        if board[i][j].is_integer():
            if board[i][j] < min:
                min_r, min_c = i, j

    return min_r, min_c

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
