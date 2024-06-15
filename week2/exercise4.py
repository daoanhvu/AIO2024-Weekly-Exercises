
def levenshtein_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    if (len1 == 0):
        return len2
    
    if (len2 == 0):
        return len1
    
    if s1[0] == s2[0]:
        return levenshtein_distance(s1[1:], s2[1:])

    pass


if __name__ == '__main__':
    print(levenshtein_distance("aab", "aba"))
