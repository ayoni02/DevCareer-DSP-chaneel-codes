def count_smileys(arr):
    #the number of valid smiley faces in array/list
    res = 0
    for i in arr:
        if len(i) > 3 or len(i) < 2:
            continue
        if len(i) == 3:
            if i[1] not in ['-', '~']:
                continue
        if i[0] in [':', ';']:
            if i[-1] in [')', 'D']:
                res += 1
    return res