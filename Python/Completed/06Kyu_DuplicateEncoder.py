def duplicate_encode(word):
    output = []
    word = word.lower()
    for x in word:
        if word.count(x) > 1:
            output.append(")")
        else:
            output.append("(")
    return "".join(output)