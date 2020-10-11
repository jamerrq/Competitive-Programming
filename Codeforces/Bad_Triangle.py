import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    m = {}
    A = list(map(int, sys.stdin.readline().split()))
    i = 0
    j = n - 2
    k = n - 1
    f = False
    while i < j:
        if A[i] + A[j] <= A[k]:
            f = True
            break
        else:
            j -= 1
    
    if f:
        print(i + 1, j + 1, k + 1)
    else:
        print(-1)
