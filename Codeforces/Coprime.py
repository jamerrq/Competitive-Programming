import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


t = read()
coprimes = {}
sup = 1001

for _ in range(t):
    n = read()
    A = readList()
    L = [-sup * sup] * sup
    for i in range(n):
        L[A[i]] = i + 1

    ans = -1
    for i in range(1, sup):
        for j in range(1, sup):
            if gcd(i, j) == 1:
                ans = max(ans, L[i] + L[j])

    print(ans)
