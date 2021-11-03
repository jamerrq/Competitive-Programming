import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    m = 0
    A = list(map(int, sys.stdin.readline().split()))
    o = [0] * n
    for i in range(1, n):
        if A[i] == A[i - 1]:
            o[i] = o[i - 1] + 1
            m = max(m, o[i])

    print(m + 1)
