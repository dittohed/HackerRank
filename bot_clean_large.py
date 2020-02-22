def next_move(posx, posy, dimx, dimy, board):
    min = dimx + dimy #max initial distance

    for (i, j) in [(x, y) for x in range(dimx) for y in range(dimy)]:
            if board[i][j] == 'd':
                distance = abs(posx - i) + abs(posy - j)
                if distance < min:
                    b_x, b_y = i, j
                    min = distance

    if b_x == posx and b_y == posy:
        print("CLEAN")
    else:
        diff_x, diff_y = b_x - posx, b_y - posy
        if diff_x > 0:
            print("DOWN")
        elif diff_x < 0:
            print("UP")
        elif diff_y > 0:
            print("RIGHT")
        elif diff_y < 0:
            print("LEFT")
