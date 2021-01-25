import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
prev = ''
ans = 0
while n:
    s = read(str)
    if s == prev:
        ans += 1
    prev = s

    n -= 1


print(ans)
