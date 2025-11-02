import math

def secretText(text):
    length = len(text)
    mid = math.floor(length / 2)
    start = text[0 : mid]
    if length % 2 != 0:
        end = text[mid+1 : length]
        new_text = end + text[mid] + start
    else:
        end = text[mid : length]
        new_text = end + start
    return new_text