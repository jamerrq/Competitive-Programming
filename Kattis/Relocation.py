import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


N, Q = readList()
locs = readList()

for _ in range(Q):
    a, b, c = readList()
    if 1 - a:
        print(abs(locs[b - 1] - locs[c - 1]))
    else:
        locs[b - 1] = c
