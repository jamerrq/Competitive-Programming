import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    P = read()
    if P % 2:
        print(2, P - 1)
    else:
        print(2, 4)
