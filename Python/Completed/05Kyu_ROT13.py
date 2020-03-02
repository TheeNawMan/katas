#There are two with this name. Complete both for some free points.

from string import ascii_lowercase as low
from string import ascii_uppercase as upr

def rot13(message):
    table = str.maketrans(low + upr, low[13:] + low[:13] + upr[13:] + upr[:13])
    return message.translate(table)