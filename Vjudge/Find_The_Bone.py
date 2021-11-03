import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n, m, k = readList()
H = set(readList())
position = 1
locked = position in H

for _ in range(k):

    u, v = readList()
    if u == position:
        if not locked:
            position = v

    elif v == position:
        if not locked:
            position = u

    locked = position in H


print(position)
