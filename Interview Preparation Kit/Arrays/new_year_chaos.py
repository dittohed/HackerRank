def minimum_bribes(q):
    bribes = 0
    reversd = 0

    for i in range(len(q)):
        diff = q[i] - i - 1 # - 1 because of 0 indexing

        if i < len(q) - 1 and q[i] > q[i + 1]:
            reversd += 1
        else:
            reversd = 0

        if diff > 2:
            print("Too chaotic")
            return
        elif diff > 0:
            bribes += diff
        elif reversd == 2:
            print("Reversed trio found!")
            bribes += 1
            reversd = 0

    print(bribes)

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimum_bribes(q)
