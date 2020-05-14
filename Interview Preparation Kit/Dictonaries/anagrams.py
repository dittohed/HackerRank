import math

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    pairs = 0

    for i in range(1, n): # substring length
        j = 0
        h_map = {}

        while j < n - i + 1: # check every substring of length i
            substr = s[j : j + i]
            hash_sum = 0

            for c in substr:
                hash_sum += hash(c) # assuming that sums will be unique

            if hash_sum in h_map:
                pairs += h_map[hash_sum]
                h_map[hash_sum] += 1
            else:
                h_map[hash_sum] = 1

            j += 1

    return pairs

q = int(input())

for q_itr in range(q):
    s = input()
    print(sherlockAndAnagrams(s))
