def selfDividingNumbers(left: int, right: int) -> List[int]:
    pl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 15, 22, 24]
    res = []
    for  i in range(left, right+1):
        if i in pl:
            res.append(i)
        else:
            if '0' in str(i):
                continue
            pla = True
            for j in str(i):
                if i%int(j)==0:
                    continue
                else:
                    pla = False
            if pla:
                res.append(i)
    return res