def countDigits(num: int) -> int:
    res = 0
    pl = []
    for i in str(num):
        if num%int(i)==0:
            res += 1
        pl.append(i)
    return res