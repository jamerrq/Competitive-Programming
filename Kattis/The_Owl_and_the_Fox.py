import sys


def bsg(i):
    big = ''
    fod = False
    for c in str(i)[::-1]:
        if c != '0' and not fod:
            big += str(int(c) - 1)
            fod = True
        else:
            big += c
    return int(big[::-1])


n = int(sys.stdin.readline())
for _ in range(n):
    j = int(sys.stdin.readline())
    print(bsg(j))
