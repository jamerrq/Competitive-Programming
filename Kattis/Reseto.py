import sys
from typing import Tuple


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


N, K = readList()
siev = [i for i in range(2, N + 1)]
prim = [False] * len(siev)

for i in range(len(siev)):
    if not prim[i]:
        for j in range(i, len(siev), siev[i]):
            if not prim[j]:
                prim[j] = True
                K -= 1
            if not K:
                print(siev[j])
                exit()
