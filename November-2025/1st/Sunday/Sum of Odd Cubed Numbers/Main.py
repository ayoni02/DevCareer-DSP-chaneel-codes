def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    res = 0
    
    for i in arr:
        if not type(i) is int:
            return None
        if i % 2:
            res += i**3
    return res