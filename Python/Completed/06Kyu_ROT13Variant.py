from string import ascii_lowercase as low
from string import ascii_uppercase as upr

def encrypter(strng):
    initial = 'abcdefghijklmnopqrstuvwxyz '
    opposite = 'zyxwvutsrqponmlkjihgfedcba '
    output = []
    a = rot13(strng)
    for x in a:
        spot = initial.index(x)
        output += opposite[spot:spot+1:]
    return "".join(output)
    
def rot13(message):
    table = str.maketrans(low + upr, low[13:] + low[:13] + upr[13:] + upr[:13])
    return message.translate(table)