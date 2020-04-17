import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a, b = min(a, b), max(a, b)
    while a > 0 and b > 0:
        if a > b:
            x = min(b, a // 2)
            if x == 0:
                break
            a -= 2 * x
            b -= x
        else:
            x = min(a, b // 2)
            if x == 0:
                break
            a -= x
            b -= 2 * x

    if a == 0 and b == 0:
        print('YES')
    else:
        print('NO')
