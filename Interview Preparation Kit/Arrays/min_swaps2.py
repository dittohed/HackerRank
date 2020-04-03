def minimum_swaps(arr):
    i = len(arr) - 1
    swaps = 0

    while i != 0:
        if arr[i] - 1 == i:
            # on the position, go left
            i -= 1
        else:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps += 1

    return swaps

arr = list(map(int, input().rstrip().split()))

print(minimum_swaps(arr))
