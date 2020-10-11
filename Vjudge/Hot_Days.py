import sys


n, m = map(int, sys.stdin.readline().split())

ans = 0

for _ in range(n):
    ti, Ti, xi, ci = map(int, sys.stdin.readline().split())
    cost = xi * m * (ti + m > Ti) + ci
    if ti < Ti:
        cost2 = ci * ((m - 1) // (Ti - ti) + 1)
        cost = min(cost, cost2)
    
    ans += cost

print(ans)
