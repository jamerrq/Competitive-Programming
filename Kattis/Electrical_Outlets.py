import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


N = read()
while N:
    K = readList()
    print(sum(K) - 2*K[0] + 1)
    N -= 1
