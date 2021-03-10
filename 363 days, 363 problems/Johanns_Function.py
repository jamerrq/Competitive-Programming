import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    #a = (2 * n ** 3 + 3 * n ** 2 + n) / 6
    #b = n * (n + 1) / 2
    result = int((n * (n + 1) * (2 * n + 1)) // 6 + (n * (n + 1)) // 2) // 2
    print(result)

