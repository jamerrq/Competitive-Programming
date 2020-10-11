import sys


t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    diff = abs(a - b)
    ans = diff // 10
    if diff - ans * 10:
        ans += 1
    print(ans)
