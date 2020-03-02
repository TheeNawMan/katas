def accum(s):
    final = []
    for i, x in enumerate(s):
            a = x.upper()
            b = x * i
            c = a + b.lower()          
            final.append(c)
    result = "-".join(final)
    return result