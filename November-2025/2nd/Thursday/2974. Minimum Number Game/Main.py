def min_num_game(num):
    arr = []
    while len(num) > 0:
        b = min(num)
        num.remove(b)
        a = min(num)
        num.remove(a)
        arr.extend([a,b])
    return arr