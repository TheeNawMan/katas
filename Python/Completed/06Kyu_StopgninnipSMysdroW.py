def spin_words(sentence):
    if len(sentence) == 0:
        return None
    split_sentence = sentence.split(" ")
    for i, word in enumerate(split_sentence):
        if len(word) >= 5:
            split_sentence[i] = word[::-1]
    print(split_sentence)
    return " ".join(word for word in split_sentence)