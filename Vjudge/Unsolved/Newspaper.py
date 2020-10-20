import sys


N = int(sys.stdin.readline())

for _ in range(N):
    mp = {}
    K = int(sys.stdin.readline())
    for _ in range(K):
        a, v = sys.stdin.readline().split()
        mp[a] = int(v)

    ans = 0
    M = int(sys.stdin.readline())
    for _ in range(M):
        line = sys.stdin.readline()
        for char in line:
            ans += mp.get(char, 0)
    
    ans /= 100
    print('{0:.2f}$'.format(ans))
