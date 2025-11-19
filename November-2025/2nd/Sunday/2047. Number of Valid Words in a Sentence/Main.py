def countValidWords(sentence: str) -> int:
        let = 'abcdefghijklmnopqrstuvwxyz'
        num = '0123456789'
        pun = '!?.,'
        hyphen = '-'

        res = 0
        for i in sentence.split():
            if len(i) < 2:
                if i in let or i in pun:
                    res += 1
                continue
                    
            if i[-1] in pun:
                i = i[:-1]
            if i[-1] == hyphen:
                continue
            pl = True
            countHyphen = 0
            for k, v in enumerate(i):
                if v in num or v in pun:
                    pl = False
                    break
                if v == hyphen:
                    if k == 0:
                        pl = False
                        break
                    countHyphen += 1
                if countHyphen > 1:
                    pl = False
                    break
            if pl == True:
                res += 1
        return res