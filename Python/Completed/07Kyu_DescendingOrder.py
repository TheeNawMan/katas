def descending_order(num):
    tostr = str(num)
    sor = sorted(tostr, reverse = True)
    numstrjoin = "".join(sor)
    final = int(numstrjoin)
    return final