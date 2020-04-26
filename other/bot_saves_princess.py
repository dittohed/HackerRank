def displayPathtoPrincess(n, grid):

    #find bot indices
    inner_break = False
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == 'm':
                m = (i, j)
                inner_break = True
                break
        if inner_break:
            break

    #find princess indices
    for (i, j) in [(x, y) for y in [0, n - 1] for x in [0, n - 1]]:
        if grid[i][j] == 'p':
            p = (i, j)

    row_diff = p[0] - m[0]
    col_diff = p[1] - m[1]

    while row_diff != 0:
        if row_diff < 0:
            print('UP')
            row_diff += 1
        else:
            print('DOWN')
            row_diff -= 1

    while col_diff != 0:
        if col_diff < 0:
            print('LEFT')
            col_diff += 1
        else:
            print('RIGHT')
            col_diff -= 1

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
