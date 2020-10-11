import sys


def get_cant(n, i):
    return (n - 1) // i + i - 1


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = 1
    r = n
    answ = n
    while l < r:
        m = (l + r) // 2
        answ = min(answ, get_cant(n, m))
    print(answ)
