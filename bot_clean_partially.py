"""
--doo
-b-oo
--doo
ooooo
ooooo

strategy: follow the pattern
"""

def next_move(posx, posy, board):
    #GENERAL IDEA: go to to_visit cells one by one and clear the environment

    if posx == to_visit[0][0] and posy == to_visit[0][1] and len(to_clean) == 0:
        to_visit.pop(0) #already visited

        for (i, j) in [(x, y) for x in (posx - 1, posx, posx + 1) for y in (posy - 1, posy, posy + 1)]:
                if i >= 0 and j >= 0 and i <= 4 and j <= 4 and board[i][j] == 'd':
                    to_clean.append((i, j))

    if len(to_clean) != 0 and posx in to_clean and posy in to_clean:
        to_clean.pop(to_clean.index((posx, posy)))
        print("CLEAN")

    if len(to_clean) == 0:
        diff_x, diff_y = to_visit[0][0] - posx, to_visit[0][1] - posy
    else:
        diff_x, diff_y = to_clean[0][0] - posx, to_clean[0][1] - posy

    if diff_x > 0:
        print("DOWN")
    elif diff_x < 0:
        print("UP")
    elif diff_y > 0:
        print("RIGHT")
    elif diff_y < 0:
        print("LEFT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    to_visit = [(1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3)] #visiting these ensure that each d will be visible
    to_clean = []
    next_move(pos[0], pos[1], board)
