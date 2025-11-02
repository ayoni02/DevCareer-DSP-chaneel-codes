import string

def insertSpace(word):
    word = word.lower().replace(" ", "")
    word = [letter for letter in word if letter not in string.punctuation]
    vowels = ["a", "e", "i", "o", "u"]
    for index in range(len(word)):
        if word[index] in vowels:
            word[index] = " " + word[index]
    return "".join(word)