import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))



t = read()
for _ in range(t):
    a, b, c = readList()
    ba = b - a
    cb = c - b
    ca = c - a
    if ca % 2 == 0 and ((c + a) // 2) % b == 0:
        print('YES')