import sys


P = int(sys.stdin.readline())

for _ in range(P):

    K, N = map(int, sys.stdin.readline().split())
    ans = 0

    for i in range(N):
        ans += i + 2

    print(K, ans)
