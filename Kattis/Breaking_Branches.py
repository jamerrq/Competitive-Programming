import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
if 1 - n % 2:
    print('Alice')
    print(1)
else:
    print('Bob')
