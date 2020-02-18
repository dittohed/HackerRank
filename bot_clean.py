"""
b---d
-d--d
--dd-
--d--
----d

greedy strategy: find the nearest one and go for it
"""

def next_move(posr, posc, board):
    min = 8 #max initial distance

    for (i, j) in [(x, y) for x in range(5) for y in range(5)]:
            if board[i][j] == 'd':
                distance = abs(posr - i) + abs(posc - j)
                if distance < min:
                    b_r, b_c = i, j
                    min = distance

    if b_r == posr and b_c == posc:
        print("CLEAN")
    else:
        diff_r, diff_c = b_r - posr, b_c - posc
        if diff_r > 0:
            print("DOWN")
        elif diff_r < 0:
            print("UP")
        elif diff_c > 0:
            print("RIGHT")
        elif diff_c < 0:
            print("LEFT")
