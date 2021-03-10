import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


T = read()
for i in range(T):
    C = readList()
    print(f'Case {i + 1}: {max(C)}')
