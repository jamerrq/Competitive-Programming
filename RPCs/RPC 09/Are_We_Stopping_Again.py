import sys


a, b, c = map(int, sys.stdin.readline().split())

stops = {}
curr = 0
ans = 0

for i in range(b, a, b):
    stops[i] = True
    ans += 1


for i in range(c, a, c):
    if stops.get(i, False):
        pass
    else:
        ans += 1


print(ans)
