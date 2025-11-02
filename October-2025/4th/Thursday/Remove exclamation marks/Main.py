def removeExclamationMarks(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] == "!":
            string[i] = ""
    string = "".join(string)
    return string