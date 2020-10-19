import sys


def cards(n):
    return (3 * n ** 2 + n) // 2


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    count = 0
    while n >= 2:
        m = int(n ** 0.5)
        while cards(m) > n:
            m -= 1
        n -= cards(m)
        count += 1
    print(count)
