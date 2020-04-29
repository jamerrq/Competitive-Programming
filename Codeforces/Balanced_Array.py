import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n % 4 != 0:
        print('NO')
    else:
        print('YES')
        odds = [2 * i + 1 for i in range(n // 2)]
        sumo = sum(odds)
        pair = [2 * (i + 1) for i in range(n // 2)]
        sump = sum(pair)
        diff = sumo - sump
        if diff < 0:
            odds[-1] += -diff
        elif diff > 0:
            pair[-1] += diff
        totl = pair + odds
        print(' '.join([str(x) for x in totl]))
