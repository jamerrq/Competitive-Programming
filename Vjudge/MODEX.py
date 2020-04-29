import sys

def binexp(a, b, mod=None):
    if b == 0:
        return 1
    res = binexp(a, b // 2)

    if b % 2 != 0:
        if mod is not None:
            b = (res * res) % mod
            c = a % mod
            return (b * c) % mod
        return res * res * a
    else:
        if mod is not None:
            res %= mod
        return (res * res) % mod


t = int(sys.stdin.readline())

for _ in range(t):
    x, y, n = map(int, sys.stdin.readline().split())
    print(binexp(x, y, n))

sys.stdin.readline()
