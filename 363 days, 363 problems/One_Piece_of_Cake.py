import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


T = read()
for _ in range(T):
    P, E = readList()
    if P - E > 9:
        print('YES')
    else:
        print('NO')
