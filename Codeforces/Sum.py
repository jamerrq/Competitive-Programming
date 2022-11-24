import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):

    a, b, c = readList()
    if c == a + b or b == a + c or a == b + c:
        print("YES")
    else:
        print("NO")