import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n, k = readList()
    #
    A = readList()
    A.sort()
    #
    M = {}
    B = {}
    P = {}
    md = 0
    for a in A:
        ma = M.get(a, 0) + 1
        M[a] = ma
        mb = M.get(a - 1, 0)
        if mb:
            B[a] = min(M[a - 1], M[a])
            if mb >= ma:
                P[a] = P[a - 1]
        else:
            P[a] = a
        
        ba = B.get(a, 0)
        if ba - a > md:
            md = ba - a
            print(a, P[a])
        else:
            print(-1)
    #