def sock_merchant(n, ar):

    dict = {}
    pairs = 0

    for item in ar:
        if item in dict:
            dict[item] += 1
            if dict[item] % 2 == 0:
                pairs += 1
        else:
            dict[item] = 1

    return pairs
