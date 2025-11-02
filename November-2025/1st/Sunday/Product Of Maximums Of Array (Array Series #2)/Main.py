def max_product(lst, n_largest_elements):
    lst.sort()
    res = 1
    for i in lst[-n_largest_elements:]:
        res *= i
    return res
