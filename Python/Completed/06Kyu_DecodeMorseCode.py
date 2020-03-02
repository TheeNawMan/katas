MORSE_CODE = {'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':'', '':' ',
                    '!':'-.-.--','SOS':'...---...'}
                    
def decodeMorse(morse_code):
    print(morse_code)
    morse_code += ' '
    decipher = ''
    citext = ''
    i = 0
    for letter in morse_code:
          if (letter != ' '):
              i = 0
              citext += letter
          else:
              i += 1
              if i == 2:
                  decipher += ''
              else:
                  decipher += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(citext)]
                  citext = ''
    final = decipher.strip()
    return final