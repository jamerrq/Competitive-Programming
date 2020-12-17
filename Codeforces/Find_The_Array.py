import sys
from math import log2


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    A = readList()
    B = []
    for i in range(n):
        num = int(log2(A[i]))
        B.append(2 ** num)

    print(*B)
