import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    if x == y:
        print('YES')
    else:
        print('NO')
