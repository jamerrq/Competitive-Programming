import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    a, b, c = sorted(readList())
    m = sum([a, b, c])
    n = m // 9
    if m % 9 == 0 and a >= n and b >= n and c >= n:
        print('YES')
    else:
        print('NO')
