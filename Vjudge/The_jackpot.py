import sys


while True:
    N = int(sys.stdin.readline())
    if not N:
        break
    bets = []
    while len(bets) < N:
        l = list(map(int, sys.stdin.readline().split()))
        bets.extend(l)

    for i in range(N):
        if i == 0:
            bets[i] = max(bets[i], 0)
        else:
            bets[i] = max(bets[i - 1] + bets[i], 0)

    if bets[-1] > 0:
        print('The maximum winning streak is {}.'.format(bets[-1]))
    else:
        print('Losing streak.')
