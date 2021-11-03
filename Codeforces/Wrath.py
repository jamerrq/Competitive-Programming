import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
L = readList()
M = [i + 1 - L[i] for i in range(n)]
N = M.copy()
for i in range(n - 2, -1, -1):
    N[i] = min(M[i], N[i + 1])


print(sum([i + 1 < N[i + 1] for i in range(n - 1)]) + 1)

