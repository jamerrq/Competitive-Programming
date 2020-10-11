import sys


t = int(sys.stdin.readline())

for _ in range(t):
    a, b, x, y, n = map(int, sys.stdin.readline().split())
    #if a < b:
    m = min(n, a - x)
    a1 = a - m
    n1 = n - m
    b1 = b - min(n1, b - y)
    #else:
    m = min(n, b - y)
    b2 = b - m
    n2 = n - m
    a2 = a - min(n2, a - x)

    print(min(a1 * b1, a2 * b2))
