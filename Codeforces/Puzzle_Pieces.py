import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if min(n, m) >= 2:
        if max(n, m) == 2:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
