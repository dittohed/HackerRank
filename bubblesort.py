def bubblesort(arr):
    n = len(arr)
    
    for i in reversed(range(1, n)): # n - 1 .. 1
        swapped = False

        for j in range(i): # 0 .. i - 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

arr = [1, 6, 3, 4, 7, 2, 1]
bubblesort(arr)
print(arr)
