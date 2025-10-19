def is_digit(n):
    #your code here
    if len(n) > 1:
        return False
    try:
        int(n)
        return True
    except:
        return False
