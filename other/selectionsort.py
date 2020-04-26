# sortowanie przez wybór
# wybieramy najmniejszy element i zamieniamy go z najniższą pozycją (ta się zmniejsza)

def selectionsort(arr):
    n = len(arr)

    for i in range(n - 1): # 0 .. n - 2
        min = i

        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

arr = [1, 6, 3, 4, 7, 2, 1]
selectionsort(arr)
print(arr)
