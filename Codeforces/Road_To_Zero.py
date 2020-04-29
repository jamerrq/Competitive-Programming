import sys

t = int(sys.stdin.readline())

for _ in range(t):

    x, y = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())

    if 2 * a < b:
        b = 2 * a

    answ = b * min(x, y)

    m = min(x, y)

    answ += a * (x + y - 2*m)
    print(answ)
