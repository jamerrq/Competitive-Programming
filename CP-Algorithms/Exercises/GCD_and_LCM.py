import sys


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a


T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(gcd(A, B), (A * B) // gcd(A, B))
