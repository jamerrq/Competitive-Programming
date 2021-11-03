import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


l, r = readList()
if l == r:
    print(l)
else:
    print(2)