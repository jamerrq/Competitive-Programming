import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
A = readList()
A.sort()


def gcd(a, b):

    while b:
        t = b
        b = a % b
        a = t

    return a


ans = A[0]
for i in range(1, n):
    ans = gcd(ans, A[i])


dec = set()
dec.add(1)
dec.add(ans)
p = 2

while ans >= p:
    if ans % p == 0:
        dec.add(p)
        ans //= p
    else:
        p += 1


print(len(dec))
