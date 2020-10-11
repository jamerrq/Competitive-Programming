import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, s, k = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))


    closed = {}
    for i in range(k):
        closed[A[i]] = True


    if not closed.get(s, False):
        print(0)
    else:
        for i in range(max(s, n - s)):
            up = min(n, s + i + 1)
            dw = max(s - i - 1, 1)
            if not closed.get(dw, False):
                print(s - dw)
                break
            if not closed.get(up, False):
                print(up - s)
                break
