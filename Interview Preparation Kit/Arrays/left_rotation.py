def rot_left(a, d):
    a_len = len(a)
    new_a = [0] * a_len

    for i in range(a_len):
        new_a[i - d % a_len] = a[i] # python supports negative indexing

    return new_a
