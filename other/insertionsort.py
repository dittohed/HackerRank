# sortowanie analogiczne do układania kart
# zaczynamy od lewej - zakładamy, że 1. karta jest już posortowana
# idziemy w prawo i dobieramy po jednej karcie umieszczając ją w odpowiednie miejsce
# np. dla 4 3 2 -> 3 4 2 -> 2 3 4 koniec

def insertionsort(arr):
    n = len(arr)
    
    for i in range(1, n):
        for j in reversed(range(i)): # i - 1 .. 0
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [7, 6, 5, 4, 3, 2, 1]
insertionsort(arr)
print(arr)
