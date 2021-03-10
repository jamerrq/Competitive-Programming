import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n, m = readList()
A, B = readList(), readList()

print(min(n, sum([x % 2 for x in B])) + min(sum([x % 2 for x in A]), m))
