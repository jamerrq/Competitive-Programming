import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    X = readList()
    S = set()
    X.sort()
    for i in range(n - 1, -1, -1):
        if X[i] + 1 in S:
            S.add(X[i])
        else:
            S.add(X[i] + 1)

    print(len(S))
