import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n, m = readList()
A = readList()
s = set()
uniques = [0] * n
for i in range(n - 1, -1, -1):
    s.add(A[i])
    uniques[i] = len(s)


for _ in range(m):
    l = read()
    print(uniques[l - 1])
