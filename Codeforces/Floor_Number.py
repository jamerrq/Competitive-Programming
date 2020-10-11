import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    if n <= 2:
        print(1)
    else:
        print(1 + (n - 3 + x) // x)
