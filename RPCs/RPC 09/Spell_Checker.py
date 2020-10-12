import sys


d = int(sys.stdin.readline())
words = {}
k = []


def ommited(wdic, wchk):

    count = 0
    i, j = 0, 0
    while i < len(wdic) and j < len(wchk):
        if count > 1:
            return False
        if wdic[i] == wchk[j]:
            i += 1
            j += 1
        else:
            count += 1
            i += 1

    return count <= 1


def added(wdic, wchk):
    count = 0
    i, j = 0, 0
    while i < len(wdic) and j < len(wchk):
        if count > 1:
            return False
        if wdic[i] == wchk[j]:
            i += 1
            j += 1
        else:
            count += 1
            j += 1

    return count <= 1


def different(wdic, wchk):

    count = 0
    i = 0

    while i < len(wdic):
        if count > 1:
            return False
        if wdic[i] != wchk[i]:
            count += 1

        i += 1

    return count == 1


def transpose(wdic, wchk):

    i = 0
    count = 0
    while i < len(wdic) - 1:
        if wdic[i] != wchk[i]:
            if wdic[i] == wchk[i + 1] and wdic[i + 1] == wchk[i]:
                count += 1
            else:
                return False

        i += 1

    return count == 1


for _ in range(d):
    word = sys.stdin.readline().strip()
    words[word] = True
    k.append(word)


n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().strip()
    print(word)
    if words.get(word, False):
        print('CORRECT')
    else:
        error = False
        for w in k:  
            if len(w) == len(word) + 1:
                if ommited(w, word):
                    error = True
                    print('ONE LETTER OMITTED FROM', w)
            if len(w) == len(word) - 1:
                if added(w, word):
                    error = True
                    print('ONE LETTER ADDED FROM', w)
            if len(w) == len(word):
                if different(w, word):
                    error = True
                    print('ONE LETTER DIFFERENT FROM', w)
                if transpose(w, word):
                    error = True
                    print('TWO LETTERS TRANSPOSED IN', w)

        if not error:
            print('UNKNOWN')

    if i < n - 1:
        print()
