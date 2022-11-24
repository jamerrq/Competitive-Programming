import sys

from sympy import rad


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()

    c = 0
    s = {}
    for num in A:
        if num in s:
            s[num] += 1
        else:
            s[num] = 1
            c += 1

    if c == n:
        print('YES')
    else:
        print('NO')