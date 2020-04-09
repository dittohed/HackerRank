def array_manipulation(n, queries):
    dict = {}

    for i in range(n):
        dict[i] = 0

    for query in queries:
        for i in range(query[0] - 1, query[1]):
            dict[i] += query[2]

    max = 0
    for item in dict.items():
        if item[1] > max:
            max = item[1]

    return max


nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

print(queries)

print(array_manipulation(n, queries))
