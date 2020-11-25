import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


s = read(str)
a = [0] * len(s)
for i in range(len(s) - 1):
    a[i] = int(s[i] == s[i + 1])
    if i:
        a[i] += a[i - 1]


a[-1] = a[-2]
print(a)
m = read()

for _ in range(m):
    l, r = readList()
    if l == r - 1:
        print(int(s[l - 1] == s[l]))
    else:
        print(a[r - 2] - a[l - 1])
