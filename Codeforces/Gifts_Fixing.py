import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    ma = min(A)
    mb = min(B)
    count = 0
    for i in range(n):
        fa = A[i] - ma
        fb = B[i] - mb
        count += max(fa, fb)
    print(count)
