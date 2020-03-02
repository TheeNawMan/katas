def order(sentence):
    dict = {}
    list = []
    split = sentence.split(" ")

    for i in split:
        for x in i:
            char = ord(x)
            if char >= ord("0") and char <= ord("9"):
                dict[x] = split.index(i)
                list.append(char - ord("0"))
                break

    list.sort()

    output = []
    for j in list:
        output.append(split[dict[str(j)]])
  
    return " ".join(i for i in output)