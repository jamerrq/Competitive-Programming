import sys

n = int(sys.stdin.readline())

for i in range(n):
    max_profit = -float('INF')
    d, s = map(int, sys.stdin.readline().split())
    for _ in range(d):
        f, t = map(int, sys.stdin.readline().split())
        if t <= s:
            if f > max_profit:
                max_profit = f
        else:
            if f - (t - s) > max_profit:
                max_profit = f - (t - s)
    
    sys.stdin.readline()
    print('Case #{}: {}'.format(i + 1, max_profit))
