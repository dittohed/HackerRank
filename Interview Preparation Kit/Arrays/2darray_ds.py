def hourglass_sum(arr):
    hours_sum = [[0] * 4] * 4 # 4x4 2D array

    for i in range(4):
        for j in range(4):
            # middle = (i + 1, j + 1)
            hours_sum[i][j] = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                                arr[i + 1][j + 1] +
                                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
            if i == 0 and j == 0:
                max = hours_sum[i][j] # mogę tak zadeklarować, bo Python nie ma bloków (takich jak np. w C++)
            if hours_sum[i][j] > max: # zasięg identyfikatora wyznacza funkcja
                max = hours_sum[i][j]

    return max
