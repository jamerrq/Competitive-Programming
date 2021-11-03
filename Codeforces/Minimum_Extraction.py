import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):

    n = read()
    A = readList()

    A.sort()
    ans = A[0]
    for i in range(1, n):
        ans = max(ans, A[i] - A[i - 1])

    print(ans)
