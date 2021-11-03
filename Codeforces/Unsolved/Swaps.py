import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    B = readList()
    minA = A[0]
    maxB = B[0]
    idx = 0
    idxA = 0
    idxB = 0
    while minA > maxB:
        idx += 1
        if A[idx] < minA:
            idxA = idx
            minA = A[idx]
        if B[idx] > maxB:
            idxB = idx
            maxB = B[idx]

    c1 = 0
    while B[c1] < minA:
        c1 += 1
    c1 += idxA
    c2 = 0
    while A[c2] > maxB:
        c2 += 1
    c2 += idxB

    print(min(c1, c2))
