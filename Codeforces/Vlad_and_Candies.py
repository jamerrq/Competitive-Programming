import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList() + [0]
    A.sort()
    if A[-1] - A[-2] > 1:
        print('no')
    else:
        print('yes')
