import sys

a, b, c, d = map(int, sys.stdin.readline().split())

while a > 0 and c > 0:
    c -= b
    a -= d

if c <= 0:
    print('Yes')
else:
    print('No')
