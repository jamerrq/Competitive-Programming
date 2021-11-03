import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()

for _ in range(t):

    x0, n = readList()
    step = 0

    if n % 4 == 1:
        step = -n
    if n % 4 == 2:
        step = 1
    if n % 4 == 3:
        step = 4 * (n // 4 + 1)

    if x0 % 2:
        print(x0 - step)
    else:
        print(x0 + step)
