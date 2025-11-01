def ordered_count(word):
    from collections import Counter
    count = Counter(word)
    # return count.most_common()
    seen = []
    for ch in count:
        if ch not in seen:
            seen.append(ch)
    return [(ch, count[ch]) for ch in seen]