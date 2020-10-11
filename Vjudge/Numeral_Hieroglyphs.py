import sys


n = int(sys.stdin.readline())


def convert(h):
    i = 0
    n = len(h)
    o = 'BUSPFTM'
    t = 0
    p = h[0]
    a = 0
    while i < n:
        c = h[i]
        if p == c:
            t += 1
        else:
            t = 0
        if t > 9 or o.index(c) > o.index(p):
            return -1
        a += 10 ** o.index(c)
        i += 1
        p = c

    return a


for _ in range(n):

    m = sys.stdin.readline().strip()[::-1]
    a = max(convert(m), convert(m[::-1]))

    if a == -1:
        print('error')
    else:
        print(a)
