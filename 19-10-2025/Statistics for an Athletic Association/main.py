def stat(strg):
    if not strg:
        return ""
    import numpy as np
    Times = [[int(y) for y in x.split('|')] for x in strg.split(', ')]
    TimesInSecs = []
    for i in Times:
        pl = 0
        pla = 0
        for j in [3600, 60, 1]:
            pla += j*i[pl]
            pl += 1
        TimesInSecs.append(pla)
    Range = max(TimesInSecs) - min(TimesInSecs)
    range = f"Range: {Range//3600:02d}|{(Range%3600)//60:02d}|{(Range%3600)%60:02d} "
    Mean = int(np.mean(TimesInSecs))
    mean = f"Average: {Mean//3600:02d}|{(Mean%3600)//60:02d}|{(Mean%3600)%60:02d} "
    Median = int(np.median(TimesInSecs))
    median = f"Median: {Median//3600:02d}|{(Median%3600)//60:02d}|{(Median%3600)%60:02d}"
    return range + mean + median
