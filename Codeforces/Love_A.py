import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


s = read(str)
a = sum([1 if s[i] == 'a' else 0 for i in range(len(s))])
print(min(len(s), 2 * a - 1))