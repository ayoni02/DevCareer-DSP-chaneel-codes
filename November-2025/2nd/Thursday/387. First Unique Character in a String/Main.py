def firstUniqChar(s):
    from collections import Counter
    count = Counter(s)
    for i in count:
        if count[i] == 1:
            return s.index(i)
    return -1