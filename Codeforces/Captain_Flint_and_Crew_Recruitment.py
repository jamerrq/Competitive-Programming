import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n > 30:
        a, b, c = 6, 10, 14
        diff = n - 30
        if diff == a or diff == b or diff == c:
            diff -= 1
            c += 1
        print('YES')
        print('{} {} {} {}'.format(a, b, c, diff))
    else:
        print('NO')
