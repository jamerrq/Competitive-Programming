import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n, a, b = readList()
chores = readList()
chores.sort()
print(chores[a + 1] - chores[a])
