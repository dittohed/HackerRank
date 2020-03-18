def print_topology(s, n):
    dict = {}
    for i in range(-n, n + 1):
        dict[i] = ['*'] * (n + 2)

    dict[0][0] = '-'
    dict[0][n + 1] = '-'

    curr_height = 0
    for pos, step in enumerate(s):
        if step == 'D':
            dict[curr_height - 1][pos + 1] = '\\'
            curr_height -= 1
        else:
            dict[curr_height][pos + 1] = '/'
            curr_height += 1

    for height in reversed(range(-n, n + 1)):
        for pos in range(n + 2):
            if dict[height][pos] != '*':
                print(dict[height][pos], end = '')
            else:
                print(' ', end = '')

        print('')

def count_valleys(s):
    curr_height = 0
    valleys = 0

    for step in s:
        if step == 'D':
            if curr_height == 0:
                valleys += 1
            curr_height -= 1
        else:
            curr_height += 1

    return valleys

n_steps = int(input())
steps = input()

print("Score: ", count_valleys(steps))
print_topology(steps, n_steps)
