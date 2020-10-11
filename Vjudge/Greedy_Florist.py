import sys


n, k = map(int, sys.stdin.readline().split())
flws = list(map(int, sys.stdin.readline().split()))

flws.sort(reverse = True)
levl = -1
ans = 0
for i in range(n):
    if not (i % k):
        levl += 1
    ans += flws[i] * (levl + 1)

print(ans)
