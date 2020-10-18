# Contest: https://vjudge.net/contest/401919#overview
import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


dic = set()
n = read()
S = readList(str)
for word in S:
    chars = set()
    for char in word:
        chars.add(char)

    s = ''.join(sorted([x for x in chars]))
    dic.add(s)


print(len(dic))
