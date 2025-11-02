def duplicate(arr):
    result = []
    for i in reversed(arr):
        if i not in result:
            result.append(i)
    return list(reversed(result))