import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    exc = {}
    tps = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        exc[(a, b)] = exc.get((a, b), 0) + 1
        tps.append((a, b))

    ans = 'YES'
    for tp in tps:
        a, b = tp
        if exc[(a, b)] != exc.get((b, a), 0):
            ans = 'NO'
            break

    print(ans)
