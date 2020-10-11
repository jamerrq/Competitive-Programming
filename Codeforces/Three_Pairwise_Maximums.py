import sys

t = int(sys.stdin.readline())

for _ in range(t):
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    if l[-1] == l[-2]:
        print('YES')
        print(l[-1], l[0], 1)
    else:
        print('NO')
