import sys
from collections import deque


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    P = readList()
    d = deque()
    l = P[0]
    for num in P:
        if num <= l:
            d.appendleft(num)
            l = num
        else:
            d.append(num)

    print(' '.join([str(x) for x in d]))
