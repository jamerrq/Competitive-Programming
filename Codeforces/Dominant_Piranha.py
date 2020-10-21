import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()

for _ in range(t):
    n = read()
    A = readList()
    a = -1

    maxi = max(A)
    for i in range(n):
        prev = maxi
        post = maxi
        if i > 0:
            prev = A[i - 1]
        if i < n - 1:
            post = A[i + 1]

        if A[i] == maxi and (prev != maxi or post != maxi):
            a = i + 1
            break

    print(a)
