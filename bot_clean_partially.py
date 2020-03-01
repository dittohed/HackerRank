def next_move(pos_x, pos_y, board, to_visit, found_d):
    #GENERAL IDEA: go to to_visit cells one by one and clear the environment by the way

    if pos_x == to_visit[0][0] and pos_y == to_visit[0][1] and len(found_d) == 0: #to_visit cell reached
        to_visit.pop(0) #already visited

        for (i, j) in [(x, y) for x in (pos_x - 1, pos_x, pos_x + 1) for y in (pos_y - 1, pos_y, pos_y + 1)]:
                if i >= 0 and j >= 0 and i <= 4 and j <= 4 and board[i][j] == 'd':
                    found_d.append((i, j))

    if len(found_d) == 0: #no cells belongs to the current to_visit cell
        cleaning_mode = False
        diff_x, diff_y = to_visit[0][0] - pos_x, to_visit[0][1] - pos_y #visit next one
    else:
        cleaning_mode = True
        diff_x, diff_y = found_d[0][0] - pos_x, found_d[0][1] - pos_y

    if diff_x > 0:
        print("DOWN")
    elif diff_x < 0:
        print("UP")
    elif diff_y > 0:
        print("RIGHT")
    elif diff_y < 0:
        print("LEFT")
    elif cleaning_mode == True and diff_x == 0 and diff_y == 0:
        found_d.pop(0)
        print("CLEAN")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    to_visit = [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3)] #visiting these ensure that each d will be visible
    found_d = []
    next_move(pos[0], pos[1], board, to_visit, found_d)
