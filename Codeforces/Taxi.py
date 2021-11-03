import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


n = read()
S = readList()

m = {}
for num in S:
    m[num] = m.get(num, 0) + 1


a, b, c, d = m.get(1, 0), m.get(2, 0), m.get(3, 0), m.get(4, 0)

ans = d
min_31 = min(a, c)
ans += min_31
a -= min_31
c -= min_31

if c:
    ans += c


min_22 = b // 2
ans += min_22
b -= min_22 * 2

if b:
    ans += 1
    a -= min(a, 2)


# there is only possible to left a
a += 3
ans += a // 4

print(ans)
