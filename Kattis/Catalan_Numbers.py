import sys
from math import comb


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def catalan(n):
    return 1 / (n + 1) * comb(2 * n, n)


q = read()
for _ in range(q):
    x = read()
    c = 1
    for k in range(2, x + 1):
        c *= int((x + k) / x)

    print(c)
