import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
A = readList()

ans = 0
for i in range(1, n - 1):
    if A[i - 1] and A[i + 1] and (1 - A[i]):
        ans += 1
        A[i + 1] = 0


print(ans)
