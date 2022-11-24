import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    a, b = readList()
    if not a:
        print(1)
    else:
        print(a + b * 2 + 1)
