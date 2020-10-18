# Contest: https://vjudge.net/contest/401919#overview
import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


n = read()
s = read(str)
m = {}
for char in s:
    m[char] = m.get(char, 0) + 1


ones = (len(s) - m.get('z', 0) * 4) // 3
ans = [1] * ones  + [0] * m.get('z', 0)
print(*ans)
