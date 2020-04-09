import sys

f = sys.stdin.readline().split('/')

f[0] = int(f[0])
f[0] -= 32 * int(f[1])

f[0] = int(f[0]) * 5
f[1] = int(f[1]) * 9

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

g = gcd(f[0], f[1])
f[0] /= g
f[1] /= g

print '%d/%d' % (f[0], f[1])

