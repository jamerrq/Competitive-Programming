import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b, c, n = map(int, sys.stdin.readline().split())
    m = max([a, b, c])
    to_complete = m - a + m - b + m - c
    remains = n - to_complete
    if remains >= 0 and remains % 3 == 0:
        print('YES')
    else:
        print('NO')
