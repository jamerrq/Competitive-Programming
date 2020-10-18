# Contest: https://vjudge.net/contest/401919#overview
import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().split()))


n = read()
P = readList()
ans = []
for i in range(n):
    curr = i + 1
    vis = set()
    while not (curr in vis):
        #print(curr, vis)
        vis.add(curr)
        curr = P[curr - 1]
        #print(i, curr, vis)

    ans.append(curr)


print(*ans)
