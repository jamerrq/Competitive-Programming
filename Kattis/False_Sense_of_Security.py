import sys

morseLetters = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '..--', '.-.-', '---.', '----']
letters = []
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.?':
    letters.append(c)
morseSymbols = ['..--', '.-.-', '---.', '----']
symbols = ['_', ',', '.', '?']
def decode(message):
    morse = ""
    lengths = ""
    for c in message:
        if c == '\n':
            pass            
        elif letters.count(c) == 1:
            morseCode = morseLetters[letters.index(c)] 
            morse += morseCode
            lengths += str(len(morseCode))
        #else:
        #    morseCode = morseSymbols[symbols.index(c)] 
        #    morse += morseCode
        #    lengths += str(len(morseCode))
    decoded = []
    count = 0
    lengthsR = ""
    for i in range(len(lengths)):
        lengthsR += lengths[len(lengths) - i - 1]
    i = 0
    while i < len(morse):
        decoded.append(morse[i : i + int(lengthsR[count])])
        i += int(lengthsR[count])
        count += 1
    toLetters = ""
    for i in decoded:
        toLetters += letters[morseLetters.index(i)]
    return toLetters

for i in sys.stdin:
    print(decode(i))
