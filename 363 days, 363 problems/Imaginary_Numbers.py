import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


while True:
    a, b = readList()

    if a + b:

        b %= 4

        if b == 0:
            print(a)
        elif b == 1:
            print(a, 'i', sep='')
        elif b == 2:
            print(-a)
        else:
            print(-a, 'i', sep='')

    else:
        break
