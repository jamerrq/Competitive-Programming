import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


k = read()
for _ in range(k):
    n = read()
    A = readList()
    A.sort()

    ans = 0
    for i in range(n):
        if A[i] <= n - i:
            ans = A[i]
        else:
            ans = max(ans, n - i)

    print(ans)
