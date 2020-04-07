import sys

t = int(sys.stdin.readline())

for _ in range(t):
    line = sys.stdin.readline().split()
    n, k = int(line[0]), int(line[1])

    if k ** 2 > n or (n - k ** 2) % 2 != 0:
        print('NO')
    else:
        print('YES')
