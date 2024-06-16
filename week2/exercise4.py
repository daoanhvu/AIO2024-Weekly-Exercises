import numpy as np


def minimum(a, b, c):
    if (a == b):
        return c if c < a else a

    if (a > b):
        if (b > c):
            return c
        else:
            return b
    else:
        # a < b
        if (c < a):
            return c
        else:
            return a


def levenshtein_distance(source, target):
    len1 = len(source)
    len2 = len(target)

    if (len1 == 0):
        return len2

    if (len2 == 0):
        return len2

    if (source == target):
        return 0

    m = len1 + 1
    n = len2 + 1
    d = np.zeros(shape=(m, n), dtype=np.int32)

    d[0][0] = 0
    # first row
    for i in range(1, n):
        d[0][i] = i
    # First colum
    for i in range(m):
        d[i][0] = i

    for r in range(1, m):
        for c in range(1, n):
            ind = 1 if (source[r-1] != target[c-1]) else 0
            d[r][c] = minimum(d[r-1, c] + 1, d[r, c-1] + 1, d[r-1, c-1] + ind)

    print(d)

    return d[len1, len2]


if __name__ == '__main__':
    # print(levenshtein_distance("execution", "intention"))
    # print(levenshtein_distance("you", "yu"))
    # print(levenshtein_distance("kitten", "sitting"))
    # print(levenshtein_distance("hi", "hello"))
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance(" hola ", " hello "))
