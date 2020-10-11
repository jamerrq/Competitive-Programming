import sys


n = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
d, m = map(int, sys.stdin.readline().split())

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + S[i]

ans = 0
#print(s)

for i in range(n - m + 1):
    #print(s[i + m], s[i])
    if s[i + m] - s[i] == d:
        ans += 1


print(ans)
