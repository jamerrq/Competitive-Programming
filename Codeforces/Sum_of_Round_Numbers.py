import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    out = []
    strn = str(n)[::-1]
    for i in range(len(strn)):
        char = strn[i]
        if char != '0':
            out.append((int(char) * 10 ** i))
    
    print(len(out))
    print(' '.join([str(x) for x in out]))
