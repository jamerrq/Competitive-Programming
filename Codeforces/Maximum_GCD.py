import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n - 1) // 2)
