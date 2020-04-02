# using bubble sort!
def minimum_bribes(q):
    bribes = 0

    for i in range(len(q)):
        diff = q[i] - i - 1 # - 1 because of 0 indexing
        if diff > 2:
            print("Too chaotic")
            return

    for i in reversed(range(n)):
        swaps = 0
        
        for j in range(0, i + 1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j] # Python swap
                swaps += 1

        bribes += swaps
        if swaps == 0:
            break

    print(bribes)

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimum_bribes(q)
