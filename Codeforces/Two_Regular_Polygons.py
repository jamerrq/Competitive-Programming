import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n, m = readList()
    if n % m == 0:
        print("YES")
    else:
        print("NO")
