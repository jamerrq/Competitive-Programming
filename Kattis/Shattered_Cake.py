import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


W = read()
N = read()
A = 0
for _ in range(N):
    wi, li = readList()
    A += wi * li

print(A // W)
