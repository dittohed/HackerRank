def nextMove(n, r, c, grid):
    #find princess indices
    for (i, j) in [(x, y) for y in range(n) for x in range(n)]:
        if grid[i][j] == 'p':
            p_r = i
            p_c = j
            break

    row_diff = p_r - r
    if row_diff != 0:
        if row_diff < 0:
            return "UP"
        else:
            return "DOWN"

    col_diff = p_c - c
    if col_diff != 0:
        if col_diff < 0:
            return "LEFT"
        else:
            return "RIGHT"

n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
