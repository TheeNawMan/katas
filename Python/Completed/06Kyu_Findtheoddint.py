from collections import Counter

def find_it(seq):
    if len(seq) == 0:
        return None
    seq_dict = Counter(seq)
    for i in seq_dict:
        if seq_dict[i] % 2 == 1:
            return i