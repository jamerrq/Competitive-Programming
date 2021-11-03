import sys


T = int(sys.stdin.readline())
for w in range(T):
    N, K = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()
    goodness = 0
    for i in range((N + 1) // 2):
        if S[i] != S[-i-1]:
            goodness += 1

    print(f'Case #{w + 1}:', abs(goodness - K))
