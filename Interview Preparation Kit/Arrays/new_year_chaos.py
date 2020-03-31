# bubble sort!
def minimum_bribes(q):
    bribes = 0
    i = len(q) - 1

    while i != 0:
        swaps = 0

        for j in range(0, i):
            if q[j] > q[j + 1]:
                temp = q[j] # TODO: use Python swap
                q[j] = q[j + 1]
                q[j + 1] = temp
                swaps += 1

                if swaps > 2:
                    print("Too chaotic")
                    return

        bribes += swaps
        i -= 1

    print(bribes)

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimum_bribes(q)
