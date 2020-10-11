import sys


t = int(sys.stdin.readline())

for _ in range(t):
    x, y, n = map(int, sys.stdin.readline().split())

    if n % x >= y:
        print(n - (n % x - y))

    else:
        opt = n - (n % x) - (9 - x)
        if opt > n:
            opt -= x
        print(opt)
