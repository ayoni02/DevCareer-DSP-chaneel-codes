def first_and_last(string):
    if len(string) > 2:
        string = list(string)
        string.pop(0)
        string.pop(-1)
        return "".join(string)
    else:
        return ""