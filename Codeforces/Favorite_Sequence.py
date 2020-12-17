import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    n = read()
    B = readList()
    A = []
    i, j = 0, n - 1
    while i < j:
        A.append(B[i])
        A.append(B[j])
        i += 1
        j -= 1

    if i == j:
        A.append(B[j])

    print(*A)
