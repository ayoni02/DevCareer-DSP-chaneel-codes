def double_appearance(s):
    single_appearance = []
    for element in s:
        if element in single_appearance:
            return element
        else:
            single_appearance.append(element)