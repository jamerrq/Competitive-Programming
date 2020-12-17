import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def steps(n):
    count = 0
    step = 1
    while n > 0:
        count += 1
        n -= step
        step += 1

    return count, n


t = read()
for _ in range(t):
    x = read()
    c, a = steps(x)
    print(x, c, c + abs(a))
