def repeatedString(s, n):
    repeated_length = len(s)
    full_occurences = n // repeated_length
    letters_left = n % repeated_length
    total_occurences = 0

    for letter in s:
        if letter == 'a':
            total_occurences += 1

    total_occurences *= full_occurences

    for i in range(letters_left):
        if s[i] == 'a':
            total_occurences += 1

    return total_occurences
