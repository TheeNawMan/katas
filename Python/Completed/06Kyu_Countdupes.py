from collections import Counter
def duplicate_count(text):
    count = 0
    a = Counter(text.lower())
    for x in a.values():
        if x > 1:
            count += 1
        else:
            count += 0
    return count