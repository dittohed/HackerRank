#TODO: rysowanko
def print_topology(s, n):
    #print('-', end = '')

    curr_height = 0
    dict = {}

    for step in s:
        if step == 'D':
            curr_height -= 1
            dict[curr_height] =


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
