import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y, n = map(int, sys.stdin.readline().split())
    resd = n % x
    coci = n // x
    m = coci * x - (y - resd + 1)
    print(m)
