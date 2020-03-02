def longest(s1, s2):
    unique_list = []
    for x in list(s1):
        if x not in unique_list:
            unique_list.append(x)
    for x in list(s2):
        if x not in unique_list:
            unique_list.append(x)
    xsort = sorted(unique_list)
    final = "".join(xsort)
    return final