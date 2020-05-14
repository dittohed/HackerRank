def split(arr, p, r):
    if p < r:
        q = (p + r) // 2

        l_arr = split(A, p, q) # sorted left part of arr
        r_arr = split(A, q, r) # sorted right part of arr

        merge(arr, p, q, r)
    else:
        return

def merge(arr, p, q, r):
    # a temporary copy is neccessary
    arr_copy = arr.copy()

    l_arr = arr_copy[p : q + 1]
    r_arr = arr_copy[q + 1 : r]

    len_l = len(l_arr)
    len_r = len(r_arr)

    for i in range(p, r + 1):
        p = 0
        r = 0

        while p < len_l and r < len_r:
            if l_arr[p] < r_arr[r]:
                arr[i] = l_arr[p]
                p += 1
            else:
                arr[i] = r_arr[r]
                r += 1

        
