import sys

t = int(sys.stdin.readline())

for _ in range(t):

    word = sys.stdin.readline().split()[0]

    if word[-1] == 'a':
        word = word + 's'
    elif word[-1] == 'i' or word[-1] == 'y':
        word = word[:-1] + 'ios'
    elif word[-1] == 'l':
        word += 'es'
    elif word[-1] == 'n':
        word = word[:-1] + 'anes'
    elif len(word) > 1 and word[-2:] == 'ne':
        word = word[:-2] + 'anes'
    elif word[-1] == 'o':
        word += 's'
    elif word[-1] == 'r':
        word += 'es'
    elif word[-1] == 't':
        word += 'as'
    elif word[-1] == 'u':
        word += 's'
    elif word[-1] == 'v':
        word += 'es'
    elif word[-1] == 'w':
        word += 'as'
    else:
        word += 'us'

    print(word)
