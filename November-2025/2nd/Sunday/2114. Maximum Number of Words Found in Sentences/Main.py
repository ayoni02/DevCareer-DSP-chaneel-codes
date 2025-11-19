def mostWordsFound(sentences: List[str]) -> int:
    res = 0

    for sentence in sentences:
        pl = sentence.split(" ")
        ln = len(pl)

        if ln > res:
            res = ln
    
    return res