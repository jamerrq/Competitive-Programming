import sys


n, k = map(int, sys.stdin.readline().split())
prcs = list(map(int, sys.stdin.readline().split()))

ans = 0
prcs.sort()
for i in range(n):
    if prcs[i] <= k:
        ans += 1
        k -= prcs[i]
    else:
        break

print(ans)
